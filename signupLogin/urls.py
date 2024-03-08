
# from registeration.views import register as reg_view, login as login_view
# from pages.views import landing_page, home_page
# from django.contrib.auth import views as authentication_view
# from django.contrib import admin
from django.urls import path,include
# from django.contrib.auth.views import LoginView
from .views import authenticationView, home,login_view,logout_view, entry_view;

urlpatterns = [
  path("accounts/", include("django.contrib.auth.urls")),
  path("signup/", authenticationView, name="authenticationView"),   
  path("", entry_view, name="home"), 
  path('login/', login_view, name='login'),
  path('logout/',logout_view, name='logout'),
  # path("home/", home, name="home"), 
]
