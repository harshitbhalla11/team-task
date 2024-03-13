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
from django.contrib import admin
from django.urls import path,include
from .views import entry_views, create_group_view
from .views import fetch_users_list
from pages.views import update_create_group,fetch_groups, group_info,group_edit, fetch_group_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(("signupLogin.urls","signupLogin"),"signupLogin")),
    path('', entry_views, name='home'),
    path('creategroup/', create_group_view, name='creategroup'),
    path('fetch_users_list/', fetch_users_list, name='fetch_users_list'),
    path('update_create_group/', update_create_group, name='update_create_group'),
    path('groups/', fetch_groups, name='Team_groups'),
    path('group/<int:group_id>/', group_info, name='group_detail'),
    path('group_edit/<int:group_id>/', group_edit, name='group_edit'),
    path('fetch_group_data/<int:group_id>/', fetch_group_data, name='fetch_group_data'),
]
