from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.admin import AdminSite

# general settings for all admin pages registered in the project
AdminSite.site_header = "Instagram Clone Admin"
AdminSite.index_title = "Instagram Clone Admin Homepage"
AdminSite.site_title = "Instagram Clone Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('account.urls')),
]

# to enable serving media files on development server
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # in dev mode mode: add the path for django toolbar (review does django toolbar disappear in production mode)
    

