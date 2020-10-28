from django.db import models

from users.models import User

class Todo(models.Model):
    task = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_done = models.BooleanField(default=False)

