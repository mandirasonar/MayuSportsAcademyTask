from rest_framework import serializers
from .models import Player
from .models import Coach

class CoachSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coach
        fields = ['user', 'team']

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ['firstName', 'lastName', 'age', 'sport', 'team']  
