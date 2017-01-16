from django.conf.urls import url, include
from .views import signup, index, login, logout, edit, menu, menu_add

urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^signup/$', signup, name='signup'),
	url(r'^login/$', login, name='login'),
	url(r'^logout/$', logout, name='logout'),
	url(r'^edit/$', edit, name='edit'),
	url(r'^menu/$', menu, name='menu'),	
	url(r'^menu/add/$', menu_add, name='menu_add'),	
]
