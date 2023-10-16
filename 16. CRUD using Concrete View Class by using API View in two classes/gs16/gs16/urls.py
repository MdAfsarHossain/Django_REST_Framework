from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    
    # List and create students data
    path('studentapi/', views.StudentListCreate.as_view()),
    
    # Retrieve, Update and Destroy students data
    path('studentapi/<int:pk>', views.StudentRetrieveUpdateDestroy.as_view()),
]
