from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.views.generic import TemplateView

# from postman.views import WriteView


admin.autodiscover()


urlpatterns = [
	# url(r'^write/(?:(?P<recipients>[^/#]+)/)?$',
 #        WriteView.as_view()(template_name='my_custom_write.html'),
 #        name='write'),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^login/$', 'django.contrib.auth.views.login'),
    # url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/crafts'}),
    url(r'^',include('crafts.urls')),
    url(r'^',include('accounts.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^messages/', include('postman.urls', namespace='postman', app_name='postman')),
    url(r'^$',TemplateView.as_view(template_name="landingpage.html")),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
