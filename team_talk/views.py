from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse


def entry_views(request):
    if request.user.is_authenticated:
        return render(request, 'home-page.html', {})    
    else:
        return render(request, 'landing-page.html', {})
    
def create_group_view(request):
    return render(request, 'create-group.html')

def fetch_users_list(request):
    users = User.objects.all()
    user_list = [{'id': user.id, 'username': user.username} for user in users]
    return JsonResponse({'users': user_list})