from django.urls import path 
from . import views 


urlpatterns = [ path('<str:palabra>/', views.verificar_palindromo, name='verificar_palindromo'), 
]

