from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from listock.models import Listock, Invitation, Category, Object, Item
        
class Command(BaseCommand):

    def add_User(self,a_name):
        user = User.objects.get_or_create(username=a_name, password='azerty')[0]
        user.save()
        return user
        
    def add_Group(self,a_name):
        a_group = Group.objects.get_or_create(name=a_name)[0]
        listock = Listock.objects.get_or_create(group = a_group)[0]
        a_group.save()
        listock.save()
        return listock
        
    def add_To_Group(self,a_user, a_group):
        a_group.user_set.add(a_user)
        a_group.save()
        
    def add_Object(self,a_name,a_category):
        object = Object.objects.get_or_create(name=a_name, category=a_category)[0]
        object.save()
        return object
        
    def add_Item(self,a_object, a_listock, a_quantityInList = 0, a_quantityInStock = 0 ):
        item = Item.objects.get_or_create(object=a_object, quantityInList=a_quantityInList, quantityInStock=a_quantityInStock, listock=a_listock)[0]
        item.save()
        return item
        
    def add_Category(self,a_name):
        category = Category.objects.get_or_create(name=a_name)[0]
        category.save()
        return category

    def _main_populate(self):

        # User 
        uMarion = self.add_User('Marion')
        uLea = self.add_User('Léa')
        uJoey = self.add_User('Joey')

        # Listock
        lColloc = self.add_Group(a_name='colloc')
        
        # Add User to Group
        self.add_To_Group(a_user=uMarion, a_group=lColloc.group)
        self.add_To_Group(a_user=uLea, a_group=lColloc.group)
        self.add_To_Group(a_user=uJoey, a_group=lColloc.group)
        
		# Fruits
        fruits = self.add_Category(a_name = 'Fruits')
		
        # Object
        bananeObject = self.add_Object(a_name='banane', a_category=fruits)
        melonObject = self.add_Object(a_name='melon', a_category=fruits)
        
        # Item
        bananeList1 = self.add_Item(a_object=bananeObject, a_quantityInList=2, a_quantityInStock = 1, a_listock=lColloc)
        melonList1 = self.add_Item(a_object=melonObject, a_quantityInList=3, a_listock=lColloc)
        
        for group in Group.objects.all():
        
            print("--- Group : " + str(group.name))
            
            print("    - Members : ")
            for user in group.user_set.all():
                print("       * " + str(user.username))
                
            print("    - Items : ")
            for item in group.listock.items.all():
                print("       | " + str(item.object.name))
                
    def handle(self,*args,**options):
        self._main_populate()
