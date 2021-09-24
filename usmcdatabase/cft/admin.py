from django.contrib import admin
from .models import Maneuver_Fire
from .models import Movement_Contact
from .models import Ammo_Lift
# Register your models here.
admin.site.register(Maneuver_Fire)
admin.site.register(Movement_Contact)
admin.site.register(Ammo_Lift)