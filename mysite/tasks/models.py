from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="profile_pics", blank=True, null=True)

    def __str__(self):
        return f"User {self.user.username} profile"