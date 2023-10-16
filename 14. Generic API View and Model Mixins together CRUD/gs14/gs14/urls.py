from django.contrib import admin
from django.urls import path
from api import views
urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Show All Data and Create data
    path('studentapi/', views.LCStudentAPI.as_view()),
    
    # Retrieve , Update and Delete student data
    path('studentapi/<int:pk>', views.RUDStudentAPI.as_view()),
]
