from django.shortcuts import render

def dashboard(request):
    return render(request, 'studentportal/student_dash.html')