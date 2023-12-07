from django.shortcuts import render, redirect
from django.http import HttpResponse
from MediConnect.models import Employee


def index(request):
    request.session.flush()
    return render(request, 'index.html')


def login(request):
    if request.method == 'GET':
        return render(request, 'login/login.html')

    if request.method == 'POST':
        empId = request.POST['empId']
        try:
            employee_info = Employee.objects.get(empid=empId, emppasswd=request.POST['empPasswd'])
            request.session['empId'] = empId
            request.session['emprole'] = employee_info.emprole
            return redirect('welcome')
        except Employee.DoesNotExist:
            return render(request, 'login/error.html')

    return HttpResponse("エラー")


def welcome(request):
    role = request.session.get('emprole')
    if role == 1:
        return render(request, 'administrator.html')
    elif role == 2:
        return render(request, 'reception.html')
    elif role == 3:
        return render(request, 'physician.html')

    return HttpResponse('エラー')


def logout(request):
    request.session.flush()
    return render(request, 'login/logout.html')


def pw_change(request):
    if request.method == 'GET':
        return render(request, 'employee/E103/pwChange.html')

    if request.method == 'POST':
        employee_info = Employee.objects.get(empid=request.session.get('empId'))
        employee_info.emppasswd = request.POST['empPasswd1']
        employee_info.save()
        return render(request, 'ok.html')


def register(request):
    if request.method == 'GET':
        if 'empId' not in request.session:
            return redirect('login')
        return render(request, 'employee/E101/register.html')

    if request.method == 'POST':
        empId = request.POST['empId']
        fName = request.POST['fName']
        lName = request.POST['lName']
        empPasswd = request.POST['empPasswd']
        empRole = int(request.POST['empRole'])

        if not Employee.objects.filter(empid=empId).exists():
            Employee(empid=empId, empfname=fName, emplname=lName, emppasswd=empPasswd, emprole=empRole).save()
            return render(request, 'ok.html')
        else:
            return HttpResponse('IDが一致しています')
