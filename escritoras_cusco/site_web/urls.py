from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='Index'),
    path('galleries', views.galleries, name='Galleries'),
    path('galleries/<int:id_escritora>', views.gallerie, name='Gallerie'),
    path('contact', views.contact, name='Contact'),
    path('about', views.about, name='About'),
    path('merci', views.merci, name='Merci')
]