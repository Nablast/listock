from django.contrib import admin
from .models import Listock, Invitation, Item, Category, Object

admin.site.register(Listock)
admin.site.register(Invitation)
admin.site.register(Item)
admin.site.register(Object)
admin.site.register(Category)