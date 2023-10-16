from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Show All Data and Create data
    # path('studentapi/', views.StudentList.as_view()),
    
    # Create student data
    # path('studentapi/', views.StudentCreate.as_view()),
    
    # Retrieve , Update and Delete student data
    # path('studentapi/<int:pk>', views.StudentRetrieve.as_view()),

    # Update Student data
    # path('studentapi/<int:pk>', views.StudentUpdate.as_view()),
    
    # Destroy Student data
    # path('studentapi/<int:pk>', views.StudentDestroy.as_view()),
    
    # List and create students data
    path('studentapi/', views.StudentListCreate.as_view()),
    
    # Retrieve and Update students data
    # path('studentapi/<int:pk>', views.StudentRetrieveUpdate.as_view()),
    
    # Retrieve and Destroy students data
    # path('studentapi/<int:pk>', views.StudentRetrieveDestroy.as_view()),
    
    # Retrieve, Update and Destroy students data
    path('studentapi/<int:pk>', views.StudentRetrieveUpdateDestroy.as_view()),
]
