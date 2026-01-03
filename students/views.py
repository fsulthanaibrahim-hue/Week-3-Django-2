from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Course
from .forms import StudentForm

def home(request):
    return render(request, 'students/home.html')


def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {
        'students': students
    })


def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})


# Renamed to student_edit for consistency with URL and template
def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.name = request.POST['name']
        student.course = request.POST['course']
        student.email = request.POST['email']
        student.save()
        return redirect('student_list')
    return render(request, 'students/student_form.html', {'student': student})


def student_delete(request, pk):  # use pk instead of id
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html', {'student': student})


def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)  # Pre-fill form with student data

    return render(request, 'students/student_form.html', {'form': form})



def course_list(request):
    query = request.GET.get('q', '')
    if query:
        courses = Course.objects.filter(name__icontains=query)
    else:
        courses = Course.objects.all()    
    return render(request, 'students/course_list.html', {
        'courses': courses
    })


def course_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        duration = request.POST.get('duration')

        Course.objects.create(
            name=name,
            duration=duration
        )
        return redirect('course_list')
    
    return render(request, 'students/course_form.html')


# Edit course
def course_edit(request, id):
    course = get_object_or_404(Course, id=id)
    if request.method == 'POST':
        course.name = request.POST.get('name')
        course.duration = request.POST.get('duration')
        course.save()
        return redirect('course_list')
    return render(request, 'students/course_form.html', {'course': course})


# Delete course
def course_delete(request, id):
    course = get_object_or_404(Course, id=id)
    course.delete()
    return redirect('course_list')

# View students in course
def course_students(request, id):
    course = get_object_or_404(Course, id=id)
    students = Student.objects.filter(course=course)
    return render(request, 'students/course_students.html', {'course': course, 'students': students})
