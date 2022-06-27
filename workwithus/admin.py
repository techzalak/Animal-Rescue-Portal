from django.contrib import admin
from .models import Signupclass

# Register your models here.
@admin.register(Signupclass)
class SignupAdmin(admin.ModelAdmin):
    list_display=('user','mobile','address','strt','lama','city','state','pin')



