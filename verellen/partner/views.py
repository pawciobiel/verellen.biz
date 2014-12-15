from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from partner.models import TearSheet, PriceList, SalesTool

def do_login(request):
    return render(request, 'partner/login.html')

def do_logout(request):
    logout(request)
    return redirect('/partner/login/')

def login_form(request):
    username = request.POST['customer_number']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            login(request, user)
            return redirect('/partner/home/')
        else:
            messages.add_message(request, messages.ERROR, 'Your account is inactive, please contact Verellen for help')
    else:
        messages.add_message(request, messages.ERROR, 'Invalid login, please check your credentials')

    return render(request, 'partner/login.html')

@login_required(login_url='/partner/login/')
def home(request):
    return render(request, 'partner/home.html')

@login_required(login_url='/partner/login/')
def sales_tools(request):
    files = SalesTool.objects.all()
    return render(request, 'partner/downloads.html', {
        'files': files
    })

@login_required(login_url='/partner/login/')
def price_lists(request):
    files = PriceList.objects.all()
    return render(request, 'partner/downloads.html', {
        'files': files
    })

@login_required(login_url='/partner/login/')
def tear_sheets(request):
    files = TearSheet.objects.all()
    return render(request, 'partner/tear_sheets.html', {
        'files': files
    })

@login_required(login_url='/partner/login/')
def account(request):
    return render(request, 'partner/home.html')
