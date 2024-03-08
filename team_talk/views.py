from django.shortcuts import render, redirect


def entry_views(request):
    if request.user.is_authenticated:
        return render(request, 'home-page.html', {})    
    else:
        return render(request, 'landing-page.html', {})