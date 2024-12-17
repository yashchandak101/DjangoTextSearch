from django.shortcuts import render,redirect
from django.http import HttpResponse
from home.forms import StudentForm
from home.models import Student, Sudent2
from django.db.models import Q

def index(request):
    context = {'form' : StudentForm}
    if request.method == "POST":

        name = request.POST.get('full_name')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        upload_file = request.FILES['upload_file']

        Sudent2.objects.create(
           name = name,
            age = age,
            gender = gender,
            upload_file  = upload_file,
        )

        print(name , age , gender)

        return redirect("/thank-you/")



    return render(request , 'index.html', context)


def contact(request):
    return render(request , 'contact.html')


def about(request):
    return render(request , 'about.html')

def dynamic_route(request, number):
    return HttpResponse(f"Response by Dynamic route you entered {number}")


def thank_you(request):
    return HttpResponse("Thank you your response is recorded")

def search_page(request):
    students = Student.objects.all()
    search = request.GET.get('search')
    age = request.GET.get('age')
    if search:
        students = students.filter(
            Q(name__icontains=search)|
            Q(email__icontains=search)|
            Q(gender__icontains=search)|
            Q(student_bio__icontains=search)|
            Q(college__college_name__icontains=search)
            )
    if age:
        if age=="1":
            students=students.filter(age__gte=18,age__lte=20).order_by('age')
        if age=="2":
            students=students.filter(age__gte=20,age__lte=25).order_by('age')
        if age=="3":
            students=students.filter(age__gte=25,age__lte=40).order_by('age')
    context = {'students' : students , 'search': search}
    return render(request , 'search.html', context)