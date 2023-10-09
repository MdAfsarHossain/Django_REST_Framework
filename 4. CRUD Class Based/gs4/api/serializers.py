from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
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
        
