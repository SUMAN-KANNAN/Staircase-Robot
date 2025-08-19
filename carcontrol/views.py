from django.shortcuts import render

# Create your views here.
def login(request):
    # return render (request, 'test.html')
    return render (request, 'Accounts /login.html')
    # return render (request, 'Include/base.html')
    # return render (request, 'landing.html')
def home(request):
    return render (request, 'Include/sidebar.html')

def control(request):
    return render (request, 'Car_control/control.html')

def landing (request):
    return render (request, 'landing.html')
    
    
    