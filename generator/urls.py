from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('password-generator/', views.password_generator, name='password_generator'),
    path('api/generate-password/', views.generate_password, name='generate_password'),
]