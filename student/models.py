from django.db import models

# Create your models here.

class Course(models.Model):
    course_name=models.CharField(max_length=30)
    
    def __str__(self):
        return self.course_name


class Student(models.Model):
    sname=models.CharField(max_length=30)
    semail=models.EmailField()
    sage=models.IntegerField()
    
    course=models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )