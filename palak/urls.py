from django.contrib import admin
from django.urls import path,include
# from palak import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('users.urls')),
    path('about/', include('users.urls')),
]