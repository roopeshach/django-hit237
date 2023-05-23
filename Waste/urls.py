
from django.urls import path
from . import views, student_views

urlpatterns = [
    path('', views.index, name="index"),
    path('student', student_views.student, name="student"),
    path('student/delete/<int:id>', student_views.delete_student, name="delete-student"),
    path('student/edit/<int:id>', student_views.edit_student, name="edit-student"),

]