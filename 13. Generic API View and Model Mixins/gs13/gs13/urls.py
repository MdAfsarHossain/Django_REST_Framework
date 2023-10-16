from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Show All Data
    path('studentapi/', views.StudentList.as_view()),
    
    # Create Data
    # path('studentapi/', views.StudentCreate.as_view()),
    
    # Get specific Data by using id
    # path('studentapi/<int:pk>', views.StudentRetrive.as_view()),
    
    # Update student data
    # path('studentapi/<int:pk>', views.StudentUpdate.as_view()),
    
    # Delete student data
    path('studentapi/<int:pk>', views.StudentDestory.as_view()),
]
