
from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm
from django.contrib import messages


def student(request):
    '''
        This function is used to render the student.html template,
        which is the page that shows the details of a student.
    '''
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully!")
            return redirect('student')
        else:
            messages.error(request, "Something went wrong!")
            print(form.errors)
            return redirect('student')

    students = Student.objects.all()
    form = StudentForm()
    context = {
        'students': students,
        'form': form
    }


    return render(request, "Waste/student.html", context)


def delete_student(request, id):
    '''
        This function is used to delete a student from the database.
    '''
    student = Student.objects.get(id=id)
    student.delete()
    messages.success(request, "Student deleted successfully!")
    return redirect('student')

def edit_student(request, id):
    '''
        This function is used to edit a student's details.
    '''
    student = Student.objects.get(id=id)
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student edited successfully!")
            return redirect('student')
        else:
            messages.error(request, "Something went wrong!")
            print(form.errors)
            return redirect('student')

    form = StudentForm(instance=student)
    context = {
        'form': form,
        'student': student,
    }
    return render(request, "Waste/edit-student.html", context)

