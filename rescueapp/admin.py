from django.contrib import admin
from .models import Message, Rescueclass
# Register your models here.
@admin.register(Rescueclass)

class RescueAdmin(admin.ModelAdmin):
  list_display = ('name','mobile','animal','img','strt','lama','city','state','pin')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
  list_display = ('id','user','msg','dt')