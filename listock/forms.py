from django import forms
from django.contrib import admin

from .models import Listock, Invitation, Category, Object, Item
		
class ObjectForm(forms.ModelForm):

	class Meta:
		model = Object
		fields = ('name',)

	#items = forms.ModelMultipleChoiceField(Item.objects.all(), required = False,)