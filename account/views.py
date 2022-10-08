from django.http import HttpResponse
from django.shortcuts import render

def profile_page(request):
    profile = request.user.profile
    
    context = {
        'profile': profile,
    }
    return render(request, 'account/profile_page.html', context)