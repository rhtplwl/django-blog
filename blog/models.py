from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='post_images', blank=True, null=True)
    created_Date = models.DateTimeField(default=timezone.now)
    published_Date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_Date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

