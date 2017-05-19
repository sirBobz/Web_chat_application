from django.conf.urls import include, url
from . import views


urlpatterns = [
  	url(r'^crafts/$', views.craft_list, name='craft_list'),
   url(r'^food/$', views.food_list, name='food_list'),
   url(r'^craft/(?P<pk>[0-9]+)/$', views.craft_detail, name='craft_detail'),
   url(r'^food/(?P<pk>[0-9]+)/$', views.food_detail, name='food_detail'),
   url(r'^new/$', views.craft_new, name='craft_new'),
   url(r'^post/(?P<pk>[0-9]+)/edit/$', views.craft_edit, name='craft_edit'),
   url(r'^drafts/$', views.craft_draft_list, name='craft_draft_list'),
   url(r'^post/(?P<pk>[0-9]+)/publish/$', views.craft_publish, name='craft_publish'),
   url(r'^post/(?P<pk>[0-9]+)/remove/$', views.craft_remove, name='craft_remove'),
   # url(r'^post/(?P<pk>[0-9]+)/comment/$', views.add_comment_to_craft, name='add_comment_to_craft'),
   url(r'^comment/(?P<pk>[0-9]+)/approve/$', views.comment_approve, name='comment_approve'),
   url(r'^comment/(?P<pk>[0-9]+)/remove/$', views.comment_remove, name='comment_remove')
]
