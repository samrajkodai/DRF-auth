from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('students', views.StudentInfo.as_view()),
    path('students/modify/<int:pk>/', views.Student.as_view()),

    path('',include('djoser.urls')),
    path('',include('djoser.urls.authtoken')),

]