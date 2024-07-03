from django.shortcuts import render

def dashboard(request):
    return render(request, 'adminportal/admin_dash.html', {})
