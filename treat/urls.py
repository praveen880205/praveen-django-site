from django.urls import path
from treat import views

urlpatterns = [
    path('',views.new),
    path('data/',views.summa),
    
]


