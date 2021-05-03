from django.contrib import admin
from post import models
# Register your models here.

@admin.register(
    models.Profile
)
class Admin(admin.ModelAdmin):
    pass

