from django.shortcuts import render, redirect
from application.models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def home(request):
    
    return render(request, 'index.html')

def aboutus(request):

    return render(request, 'about.html')

def checkrate(request):

    return render(request, 'checkrate.html')

def problem_statement(request):

    return render(request, 'services.html')

def reg(request):
    
    if request.method =='POST':
        a = request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('phone')
        d = request.POST.get('message')

        info = enquiry_table(name = a, email = b, phone = c, message = d)

        info.save()

        messages.success(request, 'Enquiry Form Submitted Successfully...')
        
    return render(request, 'contact.html')

def login_user(request):

    if request.method == 'POST':
        
        a = request.POST.get('username')
        b = request.POST.get('password')

        user = authenticate(request, username = a, password = b)

        if user is not None:
            
            login(request, user)
            # Redirect to a success page.
            return redirect('dashboard')
            
        else:
            messages.error(request, 'In-correct username or password!..')    

    return render(request, 'login.html')


def dashboard(request):

    data = enquiry_table.objects.all()

    dict1 = {'info':data}
    
    return render(request, 'dashboard/index.html', dict1)

def form_basic(request):

    return render(request, 'form_basic.html')

def form_wizard(request):

    return render(request, 'form_wizard.html')