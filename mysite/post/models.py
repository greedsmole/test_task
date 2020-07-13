from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created = models.DateField()
    last_modified = models.DateField()
    is_public = models.BooleanField(default=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
    )
    def __str__(self):
        return self.title
