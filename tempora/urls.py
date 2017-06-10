"""tempora URL Configuration
"""

from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from filebrowser.sites import site


urlpatterns = [
            url(r'^admin/', admin.site.urls),
            url(r'^upload/', include('django_file_form.urls')),
            url(r'^tinymce/', include('tinymce.urls')),
            url(r'^admin/filebrowser/', include(site.urls)),
            url(r'^grappelli/', include('grappelli.urls')), 
            ] + i18n_patterns(
                            url(r'^', include('pbhouse.urls')),
                            url(r'^profiles/', include('users.urls')),
                            url(r'^accounts/', include('allauth.urls')),
#                            url(r'^', include('blog.urls'))
                            )


if settings.DEBUG:
    urlpatterns += static(
                        settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)

