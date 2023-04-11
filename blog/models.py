from django.db import models
from django.utils import timezone
# from django.template.defaultfilters import slugify
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

# class Todo(db.Model):
#     sno = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(200), nullable=False)
#     desc = db.Column(db.String(500), nullable=False)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)

#     def __repr__(self) -> str:
#         return f"{self.sno} - {self.title}"

#     def get_absolute_url(self): 
#         return reverse('blog_post_detail', args=[self.slug])

#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.title)
#         super(Todo, self).save(*args, **kwargs)


# class Meta:
#     ordering = ['created_on']

#     def __unicode__(self):
#         return self.sno


# class Comment(models.Model):
#     name = models.CharField(max_length=42)
#     email = models.EmailField(max_length=75)
#     website = models.URLField(max_length=200, null=True, blank=True)
#     content = models.TextField()
#     post = models.ForeignKey(Todo, on_delete=models.CASCADE)
#     created_on = models.DateTimeField(auto_now_add=True)

