from django.urls import path
from Myapp import views

urlpatterns = [
  path('/', views.karibu, name='my_index'),
  path('gallery/', views.gallery, name='my_gallery'),
  path('about/', views.about, name='my_about'),
  path('contact/', views.contact, name='my_contact'),
  path('services/', views.services, name='my_services')


]
