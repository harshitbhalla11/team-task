"""
URL configuration for team_talk project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from pages.views import landing_page, home_page
from django.contrib.auth import views as authentication_view
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .views import entry_views, create_group_view
from .views import fetch_users_list
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('accounts/', include('django.contrib.auth.urls')),
    # path('register/', reg_view, name='register'),
    # path('login/', LoginView.as_view(), name='login_view'),
    path('', include(("signupLogin.urls","signupLogin"),"signupLogin")),
    # path('home/', home_page, name='home_page'),
    # path('landing/', TemplateView.as_view(template_name='landing-page.html'), name='landing'),
    path('', entry_views, name='home'),
    path('creategroup/', create_group_view, name='creategroup'),
    # path('search_users/', search_users, name='search_users'),
    path('fetch_users_list/', fetch_users_list, name='fetch_users_list'),
]
