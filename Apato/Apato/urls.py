from django.contrib import admin
from django.urls import path, include

# Static (media)
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [

    # For Admin
    path('admin/', admin.site.urls), 

    # Redirectin to user urls
    path('user/', include('user.urls')),

    # Redirectin to Listing urls
    path('listing/',include('listing.urls')),    
]

# Serve media files during development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
