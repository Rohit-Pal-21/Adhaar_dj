from django.contrib import admin
from .models import  *

# Register your models here.

@admin.register(AdhaarCardDetail)
class ViewAdmin(admin.ModelAdmin):
    pass