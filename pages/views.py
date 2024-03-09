
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User

def landing_page(request):
    return render(request, 'landing-page.html')

def home_page(request):
    return render(request, 'home-page.html')

def search_users(request):
    if request.method == 'GET' and request.is_ajax():
        query = request.GET.get('q', '')
        users = User.objects.filter(username__icontains=query).exclude(id=request.user.id)  # Exclude current user
        results = [{'id': user.id, 'text': user.username} for user in users]
        return JsonResponse({'results': results})
    return JsonResponse({'error': 'Invalid request'})