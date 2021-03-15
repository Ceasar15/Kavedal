
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from core import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', include('core.urls', namespace='home')),


]
