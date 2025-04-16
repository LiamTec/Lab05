from django.contrib import admin
from .models import Event, Participant, Registration, Attendance

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time', 'max_participants')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')

@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('event', 'participant', 'registered_at')
    list_filter = ('event',)

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('registration', 'attended')
    list_filter = ('attended',)
