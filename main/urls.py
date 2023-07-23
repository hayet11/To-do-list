from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>',views.index,name= 'index'),  #pour afficher les donnees pour chaque id 
    path('home/',views.home,name= 'home'),
    path('create/',views.create,name= 'create'),


]