from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

class Listock(models.Model):
    created_date = models.DateField(auto_now_add = True)
    lastmaj_date = models.DateField(auto_now = True)
    group = models.OneToOneField(Group, on_delete=models.CASCADE, related_name='listock')
    
    def __str__(self):
        return self.group.name
        
    def transferFromListToStock(self):
        for item in self.items :
            item.quantityInStock = item.quantityInStock + item.quantityInList
            item.quantityInList = 0
    
            
class Invitation(models.Model):
    userFrom = models.ForeignKey(User, related_name='invitationsSent')
    userTo = models.ForeignKey(User, related_name='invitations')
    listock = models.ForeignKey(Listock, related_name='invitations')
    
class Category(models.Model):
    name = models.CharField(u'Nom', max_length=255)
    
class Object(models.Model):
    category = models.ForeignKey(Category, related_name='objectsInside')
    name = models.CharField(u'Nom', max_length=255)
    description = models.CharField(u'Nom', max_length=255)
    expiryAverageTime = models.DurationField(blank=True, default=timedelta)
    image = models.ImageField(blank = True)
    
    def __str__(self):
        return self.name
    
class Item(models.Model):
    WEIGHT = 'weight'
    LIQUID = 'liquid'
    NUMBER = 'number'
    PACK = 'pack'
    NONE = 'None'
    UNITY_CHOICES = (
        (WEIGHT, 'Weight'),
        (LIQUID, 'Liquid'),
        (NUMBER, 'Number'),
        (PACK, 'Pack'),
        (NONE, 'None'),
    )
    object = models.ForeignKey(Object, related_name='items')
    quantityInList = models.IntegerField(u'Quantite', blank=True, default=0)
    quantityInStock = models.IntegerField(u'Quantite', blank=True, default=0)
    unity = models.CharField(choices = UNITY_CHOICES, default = NONE, max_length = 255)
    listock = models.ForeignKey(Listock, related_name='items')
    entryDateInStock = models.DateField(auto_now_add=True) 
    
    def __str__(self):
        return self.object.name
        
    def quantiteInListStr(self):
        return str(self.quantityInList) + ' ' + str(self.unity)
            
    def modify(self, isInList, isAdd):
        numberAdded = 0
        
        if self.unity == WEIGHT :
            numberAdded = 100;
        elif self.unity == LIQUID :
            numberAdded = 0.5;
        else :
            numberAdded =  1;
        
        if isInList and isAdd :
            self.quantityInList = self.quantityInList + numberAdded
        elif not isInList and isAdd :
            self.quantityInStock = self.quantityInStock + numberAdded
        elif isInList and not isAdd and self.quantityInList > numberAdded :
            self.quantityInList = self.quantityInList - numberAdded
        elif isInList and not isAdd and self.quantityInStock > numberAdded : 
            self.quantityInStock = self.quantityInStock - numberAdded
            
        self.listock.save()
    
        
#######################################################################################
    


        
