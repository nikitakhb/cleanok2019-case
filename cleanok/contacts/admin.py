from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(TypeContact)
class TypeContactAdmin(admin.ModelAdmin):
    pass


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass
