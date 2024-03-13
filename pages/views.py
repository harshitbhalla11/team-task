
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import Group
from django.core.serializers import serialize
import json

def landing_page(request):
    return render(request, 'landing-page.html')

def home_page(request):
    return render(request, 'home-page.html')

from django.shortcuts import render, redirect
from .models import Group

def update_create_group(request):
    if request.method == 'POST':
        group_name = request.POST.get('group_name')
        group_members = request.POST.getlist('selected_users')
        visibility_type = request.POST.get('visibility')
        description = request.POST.get('description')
        admin_user_id = request.user.id
        admin_user_name = request.user.username

        Group.objects.create(
            group_name=group_name,
            group_members=group_members,
            visibility_type=visibility_type,
            description=description,
            admin_user_id=admin_user_id,
            admin_user_name = admin_user_name
        )
        return redirect('Team_groups') 
    else:
        return render(request, 'create_group.html')
    
def fetch_groups(request):
    group_table_data = Group.objects.all()
    return render(request, 'groups.html', {'groups_data': group_table_data})


def group_info(request, group_id):
    group = Group.objects.get(pk=group_id)  
    return render(request, 'group_detail.html', {'group_data': group})

def group_edit(request, group_id):
    group = Group.objects.get(pk=group_id)  
    return render(request, 'group_edit.html', {'group_data': group})

def fetch_group_data(request, group_id):
    try:
        group = Group.objects.get(pk=group_id)
        group_data = {
            'admin_user_id': group.admin_user_id,
            'admin_user_name': group.admin_user_name,
            'group_id': group.group_id,
            'create_date_time': group.create_date_time,
            'group_members': group.group_members,
            'visibility_type': group.visibility_type,
            'description': group.description,
            'group_name': group.group_name
        }
        return JsonResponse({'group_data': group_data})
    except Group.DoesNotExist:
        return JsonResponse({'error': 'Group not found'}, status=404)