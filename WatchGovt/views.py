from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from . forms import ProjectForm
from . models import Project

def register(request):
      if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Create the user
            login(request, user)  # Log the user in
            return redirect('project_list')  # Redirect to the project list
        else:
            form = UserCreationForm()
            return render(request, 'projects/register.html', {'form': form})
    #Registration logic goes here

def login_view(request):
    def login_view(request):
     if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')  # or email if using a custom user model
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('project_list')  # Redirect to the project list
     else:
        form = AuthenticationForm()
    return render(request, 'projects/login.html', {'form': form})
   
    # Login logic goes here

def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/project_list.html', {'projects': projects})

def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'projects/create_project.html', {'form': form})

# Create your views here.
