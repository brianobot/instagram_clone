from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db.models import Q
from django.conf import settings
from django.db import models
from .managers import CustomUserManager, ProfileManager
from datetime import datetime
from decimal import Decimal
import uuid
import random

import logging
logger = logging.getLogger(__name__)

class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    ref = models.ForeignKey("self", on_delete=models.SET_NULL, blank=True, null=True)
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def followers(self):
        return self.profile.followers.count()

    @property
    def uid(self):
        return self.profile.uid

    def __str__(self) -> str:
        return str(self.email)

    def __repr__(self) -> str:
        return f"User(email='{self.email}', ref={self.ref})"


class Profile(models.Model):
    """  this model repr the database table that will hold all none auth essential details about a user, from preferences to accounts settings """    
    uid = models.CharField(max_length=100, blank=True, null=True)
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, primary_key=True)
    handle = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, default='avatars/blank_profile.png')
    followers = models.ManyToManyField('Profile', blank=True)

    is_verified = models.BooleanField(default=False, blank=True)

    # objects = ProfileManager()

    @property
    def followers_count(self):
        return self.followers.count()

    @property
    def following_count(self):
        return Profile.objects.filter(followers__handle__icontains=self.handle).count()


    @property
    def posts_count(self):
        return self.posts.count()

    def __str__(self):
        return str(self.handle)

    def __repr__(self):
        return f'<Profile(email={self.handle})>'    

    def save(self, *args, **kwargs):
        if not self.handle:
            self.handle = f"@{self.user.email.split('@')[0]}"
        super().save(*args, **kwargs)
