from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from root.settings import MEDIA_URL, MEDIA_ROOT, DEBUG, STATIC_URL, STATIC_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.urls'))
]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
    urlpatterns += static(STATIC_URL, document_root=STATIC_ROOT)
