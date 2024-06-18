from django.contrib import admin
from models.models import Event, Attendee
class EventAdmin(admin.ModelAdmin):
    list=('name', 'description','date','time','location','capacity')
class AttendeeAdmin(admin.ModelAdmin):
    list=('name', 'email','event')
admin.site.register(Event, EventAdmin)
admin.site.register(Attendee, AttendeeAdmin)

# Register your models here.
