from django.db import models
from account.models import Profile


class ShareableMedia(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    caption = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        abstract = True


class Post(ShareableMedia):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    media = models.FileField(upload_to='posts/%Y/%m/%d/')

    def __str__(self):
        return f"Post by {self.profile}"

    def __repr__(self) -> str:
        return f"Post(profile={self.profile})"


class Story(ShareableMedia):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='stories')
    media = models.FileField(upload_to='stories/%Y/%m/%d/')

    class Meta:
        verbose_name_plural = 'Stories'

    def __str__(self):
        return f"Story by {self.profile}"

    def __repr(self):
        return f"Story(profile={self.profile})"


class HighLight(ShareableMedia):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='highlights')
    media = models.FileField(upload_to='highlights/%Y/%m/%d/')

    class Meta:
        verbose_name_plural = 'HighLights'

    def __str__(self):
        return f"HighLight by {self.profile}"

    def __repr(self):
        return f"HighLight(profile={self.profile})"
