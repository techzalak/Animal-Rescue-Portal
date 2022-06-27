from django.contrib import admin
from .models import Donateclass      #donateclass is class name
# Register your models here.

@admin.register(Donateclass)
class DonateAdmin(admin.ModelAdmin):
    list_display=('id','name','email','mobile','comment','add','anony','amt')