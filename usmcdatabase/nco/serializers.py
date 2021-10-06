from rest_framework import serializers
from .models import Nco


class NcoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nco
        fields = ['id', 'username', 'password',
                  'email', 'first_name', 'last_name']