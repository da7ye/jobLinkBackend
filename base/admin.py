from django.contrib import admin
from .models import Category, Provider


admin.site.register(Provider)
admin.site.register(Category)