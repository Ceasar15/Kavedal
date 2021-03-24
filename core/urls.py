from django.conf.urls import url
from django.urls import path
from core import views
from django.conf.urls.static import static
from Kavedal import settings

urlpatterns = [
    path('', views.home, name=''),
    # path('contact/', views.contact, name='contact'),

] 
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)