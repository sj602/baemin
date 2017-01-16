from django.conf.urls import url, include
from .views import signup, index, login, logout, edit, menu_list, menu_add, menu_detail, menu_edit
urlpatterns = [
	url(r'^$', index, name='index'),
	url(r'^signup/$', signup, name='signup'),
	url(r'^login/$', login, name='login'),
	url(r'^logout/$', logout, name='logout'),
	url(r'^edit/$', edit, name='edit'),
	url(r'^menu/$', menu_list, name='menu_list'),	
	url(r'^menu/add/$', menu_add, name='menu_add'),	
	url(r'^menu/(?P<menu_id>\d+)/$', menu_detail, name='menu_detail'),
	url(r'^menu/(?P<menu_id>\d+)/$', menu_edit, name='menu_edit'),
]
