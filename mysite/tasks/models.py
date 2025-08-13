from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return self.name
