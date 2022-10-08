from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from .models import  Profile

import logging 
logger = logging.getLogger(__name__)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance, created, **kwargs):
    """creates a profile instance for the justed created user
       otherwise just save the profile instance
    """
    if created:
        profile = Profile.objects.create(user=instance)
    else:
        instance.profile.save()
