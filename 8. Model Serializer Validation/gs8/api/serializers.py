from rest_framework import serializers
from .models import Student


# Validators
def start_with_r(value):
    if value[0].lower() != 'a':
        raise serializers.ValidationError('Name should be start with A')


class StudentSerializer(serializers.ModelSerializer):
    
    name = serializers.CharField(validators=[start_with_r]) 
    
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']
    
    
    # Field label validation methods
    def validate_roll(self,value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full!')
        return value
    
    
    # Object label validation methods
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        
        if nm.lower() == 'yucca' and ct.lower() != 'rng':
            raise serializers.ValidationError('City must be RNG')
        return data
        
