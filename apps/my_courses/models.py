from __future__ import unicode_literals
from django.db import models
from django.contrib import messages

class Course_Manager(models.Manager):
    def create(self, request):
        is_valid = True
        if len(request.POST["name"]) < 1:
            messages.error(request, "Course Name cannot be blank")
            is_valid = False
        if not is_valid:
            return False
        new_course = Course (
                name = request.POST["name"],
                description = request.POST["description"]
            )
        new_course.save()

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    course_manager = Course_Manager()