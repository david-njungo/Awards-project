from django.shortcuts import render
from .models import Projects
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/accounts/login/')
def home(request):
    # projects = Projects.get_project()
    projects = Projects.objects.all()
    return render(request, 'home.html',{"projects" : projects})
