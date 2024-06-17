from django.shortcuts import redirect, render

from app.models import Employee

# Create your views here.


def register(request):
    if request.method == 'POST':
        ename = request.POST['name'] 
        eemail = request.POST['email']
        eactive = request.POST['active']
        epassword = request.POST['password']

        user = Employee(ename=ename,eemail=eemail,eactive=eactive,epassword=epassword)
        user.save()
    emp=Employee.objects.all()

    return render(request,'register.html',{"emp":emp})