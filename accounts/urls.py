from django.conf.urls import include, url

from . import views

urlpatterns = [
        url(r'^register/$', views.register,name="register"),
        # url('^logout', views.logout_view,name="logout"),
        # url('^login', views.logout_view,name="login"),
        url(r'^password_change/$','django.contrib.auth.views.password_change',{'template_name': 'profiles/change-password.html'}),
        url(r'^password_change/done',
    'django.contrib.auth.views.password_change_done',
    {'template_name':'profiles/password_change_done.html'}),

        url(r'^login/$', 'django.contrib.auth.views.login'),
        url(r'^logout/$', 'django.contrib.auth.views.logout',
                          {'next_page': '/'}),
        url(r'^', include('django.contrib.auth.urls')),
        url(r'^myprofile/$', views.myprofile, name='myprofile'),
        url(r'^users/$', views.user_profilelist, name='user_profilelist'),
        url(r'^editprofile/$', views.profile_edit, name='profile_edit'),
        url(r'^(?P<id>\d+)$', views.user_profiles, name='user_profiles'),


]
