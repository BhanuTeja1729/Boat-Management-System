from django.contrib import admin
from .models import boat_details,user_details,ride_booking
# Register your models here.

admin.site.register(boat_details)
admin.site.register(user_details)
admin.site.register(ride_booking)

