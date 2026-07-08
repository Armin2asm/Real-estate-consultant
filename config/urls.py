from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Apps
    
    path('Home/', include('HomePage.urls')),
    path('Agents/', include('Agents.urls')),
    path('Accounts/', include('Accounts.urls')),
    path( "Properties/",    include(("Properties.urls", "properties"), namespace="properties")),

    # ✅ Language switch endpoint
    path('i18n/', include('django.conf.urls.i18n')),
]


# Media files (development)
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )