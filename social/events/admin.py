from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(AddUser)
class AddUserAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'phone', 'address', 'relationship')