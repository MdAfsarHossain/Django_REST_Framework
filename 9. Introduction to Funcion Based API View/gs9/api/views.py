from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
# @api_view()
# def hello_world(request):
#     return Response({'msg': 'Hello World!!'})

# Same as the above
# @api_view(['GET'])
# def hello_world(request):
#     return Response({'msg': 'Hello World!!'})

# @api_view(['POST'])
# def hello_world(request):
#     if request.method == 'POST':
#         print(request.data)  # Server site
#         return Response({'msg': 'This is a POST request!'})

@api_view(['GET','POST'])
def hello_world(request):
    if request.method == 'GET':
        return Response({'msg': 'This is a GET request!'})
    
    if request.method == 'POST':
        print(request.data)  # Server site
        return Response({'msg': 'This is a POST request!', 'data': request.data})