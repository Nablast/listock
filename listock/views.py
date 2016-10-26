from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Listock, Invitation, Category, Object, Item
from django.contrib.auth.decorators import login_required

from .forms import ObjectForm

# Create your views here.

@login_required
def menu(request):
    return render(request, 'listock/listock_menu.html', {})
  
@login_required  
def listock_new(request,pk):
    user = get_object_or_404(Group, pk=pk)
    return render(request, 'listock/listock_new.html',{'user' : user})
    
    #####################################
    ############ Invitation #############
    #####################################
   
@login_required
def invitations(request,pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'listock/listock_invitations.html', {'invitations' : user.invitations})

@login_required    
def listock_invite(request,pk1,pk2):
    user = get_object_or_404(Group, pk=pk1)
    users = User.objects.all()
    listock = get_object_or_404(Listock, pk=pk2)
    return render(request, 'listock/listock_invite.html', {'user' : user, 'listock' : listock, 'allUsers' : users})
    
    #####################################
    ############## Listock ##############
    #####################################

@login_required    
def list(request,pk):
    listock = get_object_or_404(Listock, pk=pk)
    return render(request, 'listock/listock_list.html',{'listock' : listock})

@login_required    
def stock(request,pk):
    listock = get_object_or_404(Listock, pk=pk)
    return render(request, 'listock/listock_stock.html',{'listock' : listock})

@login_required    
def items(request,pk):
    listock = get_object_or_404(Listock, pk=pk)
    allItems = Object.objects.all()
    return render(request, 'listock/items.html',{'favorites' : listock.items, 'itemsList' : allItems})    

    #####################################
    ############## Object ###############
    #####################################

@login_required    
def object_new(request,pk):
    listock = get_object_or_404(Listock, pk=pk)
    if request.method == "POST":
        form = ObjectForm(request.POST)
        if form.is_valid():
            object = form.save()
            return redirect('listock.views.listock_detail', pk=pk)
    else:
        form = ObjectForm()
    return render(request, 'listock/object_new.html', {'listock':listock, 'form': form })
