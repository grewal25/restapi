from django.contrib import admin

# Register your models here.
from .models import Choice, Post

admin.site.register(Post)
admin.site.register(Choice)
