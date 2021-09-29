from django.shortcuts import render,redirect,reverse
from .models import Projects,Profile
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import ProfileSerializer,ProjectsSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly

# Create your views here.

def home(request):
    # projects = Projects.get_project()
    projects = Projects.objects.all()
    return render(request, 'home.html',{"projects" : projects})

def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Projects.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

#.....
@login_required(login_url='/accounts/login/')
def profile_page(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)          
        return redirect('myprofile')

    else:
        form = ProfileForm()
    return render(request, 'profile.html', {"form": form})

class ProfileList(APIView):
    def get(self,request,format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles,many=True)
        return Response(serializers.data)
    permission_classes = (IsAdminOrReadOnly,)

class ProjectsList(APIView):
    def get(self,request,format=None):
        all_projects = Projects.objects.all()
        serializers = ProjectsSerializer(all_projects,many=True)
        return Response(serializers.data)
    permission_classes = (IsAdminOrReadOnly,)