from django.contrib import admin
from blog.models import Todo,Messages,Post,Profile

admin.site.register(Todo)
admin.site.register(Messages)
admin.site.register(Post)
admin.site.register(Profile)
