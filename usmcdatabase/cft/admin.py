from django.contrib import admin
from .models import Movement_Contact, Maneuver_Fire, Ammo_Lift
# Register your models here.
admin.site.register(Movement_Contact, Maneuver_Fire, Ammo_Lift)