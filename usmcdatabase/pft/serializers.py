from rest_framework import serializers
from .models import Three_Mile, Row, Crunches, Plank, Pullups, Pushups



class Three_MileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Three_Mile
        fields = ['id', 'gender', 'age',
                  'time', 'score', 'high_alt']
        
class RowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Row
        fields = ['id', 'gender', 'age',
                  'time', 'score', 'high_alt']
        
class CrunchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crunches
        fields = ['id', 'gender', 'age',
                  'reps', 'score']
        
class PlankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plank
        fields = ['id', 'gender', 'age',
                  'time', 'score']

class PullupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pullups
        fields = ['id', 'gender', 'age',
                  'reps', 'score']

class PushupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pushups
        fields = ['id', 'gender', 'age',
                  'reps', 'score']

