from django.contrib import admin
from .models import Profesional

# Register your models here.
class ProfesionalAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'profesion', 'created')

admin.site.register(Profesional)
