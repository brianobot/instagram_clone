from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('profile/', views.profile_page, name='profile-page'),
]