from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from django.conf import settings
from django.conf.urls.static import static

handler404 = 'Globals.views.NotFound'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
    path('auth/', include('Authentication.urls')),
    path('blog/', include('Blog.urls')),
    path('dashboard/', include('Dashboard.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] 
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)