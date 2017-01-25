from django.shortcuts import render, redirect
from models import Course
# Create your views here.
def index(request):
    course = Course.objects.all()
    context = {
        "courses": course
    }
    return render(request, "my_courses/index.html", context)

def add(request):
    Course.course_manager.create(request)
    return redirect("/")

def destroy(request, course_id):
    course = Course.objects.get(id=course_id)
    course.delete()
    return redirect("/")