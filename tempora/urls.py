"""tempora URL Configuration
"""

from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin


urlpatterns = [
            url(r'^admin/', admin.site.urls),
            ] + i18n_patterns(
                            url(r'^', include('pbhouse.urls'))
                            )


if settings.DEBUG:
    urlpatterns += static(
                        settings.MEDIA_URL,
                        document_root=settings.MEDIA_ROOT)

