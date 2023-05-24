
from django.urls import path
from . import views, student_views, waste_type_views

urlpatterns = [
    path('', views.index, name="index"),
    path('student', student_views.student, name="student"),
    path('student/delete/<int:id>', student_views.delete_student, name="delete-student"),
    path('student/edit/<int:id>', student_views.edit_student, name="edit-student"),
    path('waste-type', waste_type_views.waste_type, name='waste-type'),
    path('waste-type/delete/<int:id>', waste_type_views.delete_waste_type, name='delete-waste-type'),
    path('waste-type/edit/<int:id>', waste_type_views.edit_waste_type, name='edit-waste-type'),


]