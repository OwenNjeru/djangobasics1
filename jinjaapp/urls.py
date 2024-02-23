from django.urls import path
from jinjaapp import views

urlpatterns = [
    path('', views.karibu),
    path('home/', views.myhome, name='my_index'),
    path('about/', views.about,name='my_about'),
    path('contact/', views.contact,name='my_contact'),
    path('gallery/',views.gallery,name='my_gallery'),
    path('services/',views.services,name='my_services')
]
