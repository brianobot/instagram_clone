import factory
from .models import User, Profile
from django.db import models

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('email', 'id')
    
    id = factory.Sequence(lambda n: n + 1)
    email = factory.Sequence(lambda n: f"user_{n}@example.com")
    password = 'testpassword12secure'

class ProfileFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Profile
        django_get_or_create = ('user',)

    user = factory.SubFactory(UserFactory, profile=None) #the addition of profile=None is a measure to fix duplicate user keys in factory boy
    bio = 'default user bio'
    