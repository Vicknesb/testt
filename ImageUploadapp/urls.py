from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from .views import register,login_user,logout_user,upload,success,display,searchImage

urlpatterns = [
    path('', login_user, name="login_user"),
    path('register/', register, name="register"),
    path('logout_user/', logout_user, name="logout_user"), 
    path('image_upload', upload, name='image_upload'),
    path('success', success, name='success'), 
    path('display_image', display, name='display_image'),
    path('search_image',searchImage , name='search_image'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
