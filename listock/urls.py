from django.conf.urls import url
from . import views
	
urlpatterns = [
	url(r'^$', views.menu, name='menu'),
	url(r'^listock/(?P<pk>[0-9]+)/list$', views.list, name='listock_list'),
	url(r'^listock/(?P<pk>[0-9]+)/stock$', views.stock, name='listock_stock'),
	url(r'^listock/(?P<pk>[0-9]+)/invitations$', views.invitations, name='listock_invitations'),
	url(r'^listock/(?P<pk>[0-9]+)/items$', views.items, name='listock_items'),
]