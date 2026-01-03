from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)  # optional

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)

    def __str__(self):
        return self.name


