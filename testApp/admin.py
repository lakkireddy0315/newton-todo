from django.contrib import admin
from .models import Blog,BlogCategory,Student

# Register your models here.
admin.site.register(Blog)
admin.site.register(BlogCategory)
admin.site.register(Student)
