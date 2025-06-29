from django.urls import path  

from . import views

urlpatterns = [
    path('',views.homefunction,name='home'),
    path('<int:pk>/', views.portfolio_detail, name='portfolio_detail'),
    path('contact/', views.contact_f, name='contact'),
    
]
