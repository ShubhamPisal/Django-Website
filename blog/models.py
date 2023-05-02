from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
# from django.template.defaultfilters import slugify # used to give outpun in the specified manaer
# from django.urls import reverse

# Create your models here.
class Todo(models.Model):
    sno = models.AutoField(auto_created = True, primary_key=True)
    title = models.TextField(max_length=255)
    desc = models.TextField(max_length=255)
    created_on = models.DateTimeField(default=timezone.now)

    def __repr__(self):
        return f"{self.sno} - {self.title} - {self.desc}"

# Created your Todo table.
class Messages(models.Model):
    sno = models.AutoField(auto_created = True, primary_key=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    message = models.TextField(max_length=255)
    created_on = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)

    def __repr__(self):
        return f"{self.sender} - {self.message} -  {self.recipient}"

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)