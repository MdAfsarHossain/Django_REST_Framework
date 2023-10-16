from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# List and Create a list of students data
class StudentListCreate(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# Retrieve, Update and Distory a list of students data
class StudentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
