from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from django.conf import settings

urlpatterns = [
    path('traids/', include('traids.urls')),
    path('search/', include('search.urls')),
    path('contacts/', include('contacts.urls')),
    path('cabinet/', include('cabinet.urls')),
    path('product/', include('product.urls')),
    path('admin/', admin.site.urls),
    path('', include('auth_user.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
