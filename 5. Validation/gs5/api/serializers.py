from rest_framework import serializers
from .models import Student


# Validators
def start_with_r(value):
    if value[0].lower() != 'a':
        raise serializers.ValidationError('Name should be start with A')


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100, validators=[start_with_r])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)
    

    def create(self, validation_data):
        return Student.objects.create(**validation_data)
    
    def update(self, instance, validation_data):
        print(instance.name)
        instance.name = validation_data.get('name', instance.name)
        print(instance.name)
        instance.roll = validation_data.get('roll', instance.roll)
        instance.city = validation_data.get('city', instance.city)
        instance.save()
        return instance
    
    
    # Field label validation methods
    def validate_roll(self,value):
        if value >= 200:
            raise serializers.ValidationError('Seat Full!')
        return value
    
    
    # Object label validation methods
    def validate(self, data):
        nm = data.get('name')
        ct = data.get('city')
        
        if nm.lower() == 'afsar' and ct.lower() != 'ctg':
            raise serializers.ValidationError('City must be CTG')
        return data
        
