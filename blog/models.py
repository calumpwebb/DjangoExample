from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    class Meta:
        ordering = ("-date_posted",)

    title = models.CharField(max_length=128)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    # if a USER is deleted, delete the POST as well
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
