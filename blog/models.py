from django.db import models
from django.utils import timezone
# from django.template.defaultfilters import slugify # used to give outpun in the specified manaer
# from django.contrib.auth.models import User
# from django.urls import reverse

# Create your models here.
class Todo(models.Model):
    sno = models.AutoField(auto_created = True, primary_key=True)
    title = models.TextField(max_length=255)
    desc = models.TextField(max_length=255)
    created_on = models.DateTimeField(default=timezone.now)

    # def __repr__(self) -> str:
    #     return f"{self.sno} - {self.title}"

# Created your Todo table.
class Messages(models.Model):
    sno = models.AutoField(auto_created = True, primary_key=True)
    message = models.TextField(max_length=255)
    created_on = models.DateTimeField(default=timezone.now)