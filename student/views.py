from django.shortcuts import render,redirect
from .models import Student
from django.contrib import messages
# Create your views here.
def get_student(request):
    students=Student.objects.all()
    return render(request,'student_list.html',{'data':students})

def add_student(request):
    if request.method== "POST":
        name=request.POST['name']
        email=request.POST['email']
        age=request.POST['age']

         #validation
        if not name or not email or not age:
            messages.error(request,"All Filed is required")
            return redirect('add_student')
        if not name.isalpha ():
            messages.error(request,"Name must contain letter..")
            return redirect('add_student')
        if int(age) < 0 or int(age) > 100:
            messages.error(request,"Age must be greater than 1 and 100")
            return redirect('add_student')
       

        Student.objects.create(sname=name,semail=email,sage=age)
        messages.success(request, "Student added successfully")
        return redirect('student_list')
    return render(request,'add_student.html')

def edit_student(request,id):
    student=Student.objects.get(id=id)
    if request.method=="POST":
        student.sname=request.POST['name']
        student.semail=request.POST['email']
        student.sage=request.POST['age']
        student.save()
        return redirect('student_list')
    return render(request,'edit_student.html',{'data':student})

def delete_student(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect('student_list')

