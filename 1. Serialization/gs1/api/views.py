from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

# Create your views here.

# Model Object - Single Student Data
def student_detail(request, pk):
    # stu = Student.objects.get(id = 1)
    # stu = Student.objects.get(id = 2)
    stu = Student.objects.get(id = pk)
    # stu = Student.objects.all()
    serializer = StudentSerializer(stu)  # Convert Python
    
    return JsonResponse(serializer.data)
    # json_data = JSONRenderer().render(serializer.data) # Convert JSON format
    
    # Print All the element
    # print(stu)
    # print(serializer)
    # print(serializer.data)
    # print(json_data)
    
    # return HttpResponse(json_data, content_type='application/json')




# Query Sel - All Student Data
def student_list(request):
    stu = Student.objects.all()
    serializer = StudentSerializer(stu, many=True)  # Convert Python
    return JsonResponse(serializer.data, safe=False)
    
    # json_data = JSONRenderer().render(serializer.data) # Convert JSON format
    
    # Print All the element
    # print(stu)
    # print(serializer)
    # print(serializer.data)
    # print(json_data)
    
    # return HttpResponse(json_data, content_type='application/json')