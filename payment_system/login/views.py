from django.shortcuts import render, redirect
from adminportal.serializers import LoginSerializer
from django.contrib.auth import logout
from rest_framework.decorators import api_view

def login(request):
    context = {}
    context['is_error'] = False
    context['error'] = ''
    return render(request, 'login/login.html', context)


def do_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/login/')


@api_view(['POST'])
def login_validation(request):
    if request.method == 'POST':
        mn = LoginSerializer(data=request.data)
        context = {}
        if mn.is_valid():
            request.session['logged_in'] = True
            return redirect('/adm/dashboard/')
        context['is_error'] = True
        context['error'] = mn.errors['non_field_errors'][0]
        return render(request, 'login/login.html', context)
