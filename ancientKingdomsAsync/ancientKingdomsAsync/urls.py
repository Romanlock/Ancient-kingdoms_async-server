from django.contrib import admin
from django.urls import path
from kingdoms import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', views.set_status, name='set-status'),
]