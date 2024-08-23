from django.urls import path
from . import views  # Make sure this import is correct

urlpatterns = [
    path('', views.home, name='home'),  # Example URL pattern
 #   path('login/', views.login_user, name='login'),  # Example URL pattern
    path('logout/', views.logout_user, name='logout'),  # Example URL pattern
    path('register/', views.register_user, name='register'),
]
