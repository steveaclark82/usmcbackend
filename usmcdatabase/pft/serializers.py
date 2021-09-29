from rest_framework import serializers
from .models import Three_Mile, Row, Crunches, Plank, Pullups, Pushups



class PftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Three_Mile
        fields = ['id', 'gender', 'age',
                  'time', 'score', 'high_alt']
        
class PftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Row
        fields = ['id', 'gender', 'age',
                  'time', 'score', 'high_alt']
        
class PftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crunches
        fields = ['id', 'gender', 'age',
                  'reps', 'score']
        
class PftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plank
        fields = ['id', 'gender', 'age',
                  'time', 'score']

class PftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pullups
        fields = ['id', 'gender', 'age',
                  'reps', 'score']

class PftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pushups
        fields = ['id', 'gender', 'age',
                  'reps', 'score']
