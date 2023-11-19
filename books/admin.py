from django.contrib import admin
from django.contrib.auth.models import User, Group

from .models import Book

# Register your models here.


admin.site.register(Book)


class CustomAdminSite(admin.AdminSite):
    def get_registered_model(self, model):
        if model != User and model != Group:
            return super().get_registered_model(model)
        return None
