from rest_framework import serializers
from .models import Student


class StudentSerializer(serializers.ModelSerializer):
    
    # Way: 1
    # name = serializers.CharField(read_only=True)
    
    class Meta:
        model = Student
        fields = ['id', 'name', 'roll', 'city']

        # Way: 2
        # read_only_fields = ['name', 'roll']
        
        # Way: 3
        extra_kwargs = {'name': {'read_only': True}}
