from rest_framework import serializers
from .models import Movement_Contact, Maneuver_Fire, Ammo_Lift

class Movement_ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movement_Contact
        fields = ['id', 'gender', 'age', 'time', 'score', 'high_alt']
        

class Maneuver_FireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maneuver_Fire
        fields = ['id', 'gender', 'age', 'time', 'score', 'high_alt']
        
class Ammo_LiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ammo_Lift
        fields = ['id', 'gender', 'age', 'reps', 'score']
