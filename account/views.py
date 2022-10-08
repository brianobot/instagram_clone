from django.http import HttpResponse
from django.shortcuts import render

def profile_page(request):
    profile = request.user.profile
    return HttpResponse(f"""
        Profile Page ....for <a href="#"><b>{profile.handle}</b></a><br/> 
        Followers : {profile.followers_count}<br/>
        Following : {profile.following_count}<br/>
        <hr/>
        Posts: {profile.posts.count()}<br/>
        Stories: {profile.stories.count()}<br/>
        HightLights: {profile.highlights.count()}<br/>
        """)