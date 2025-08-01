from django.contrib import admin
from .models import Reservation, Slot, Resource, Facility

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'slot', 'created_at', 'status')
    list_filter = ('status',)
    search_fields = ('user__email', 'slot__start_time')

@admin.register(Slot)
class SlotAdmin(admin.ModelAdmin):
    list_display = ('title', 'resource', 'start_time', 'end_time', 'is_booked')
    filter_horizontal = ("facilities",) 

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name', 'location')

@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ("name", "icon")
    search_fields = ("name",)