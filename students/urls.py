from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.student_list, name='student_list'),
    path('add/', views.student_create, name='student_create'),
    path('edit/<int:pk>/', views.student_update, name='student_edit'),  # ✅ This is important
    path('delete/<int:pk>/', views.student_delete, name='student_delete'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/add/', views.course_create, name='course_create'),
    path('courses/edit/<int:id>/', views.course_edit, name='course_edit'),   # edit
    path('courses/delete/<int:id>/', views.course_delete, name='course_delete'), # delete
    path('courses/<int:id>/students/', views.course_students, name='course_students'), # view students
]
