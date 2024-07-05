from django.shortcuts import render
import datetime

def dashboard(request):
    today = datetime.datetime.now()
    current_date = today.strftime('%d-%m-%Y')
    return render(request, 'studentportal/student_dash.html', {'current_date' : current_date})
