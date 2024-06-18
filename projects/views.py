from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Project
from .forms import ProjectForm


@login_required
def dashboard(request):
    completed_projects = Project.objects.filter(status='completed').count()
    in_progress_projects = Project.objects.filter(status='in_progress').count()
    return render(request, 'dashboard.html', {
        'completed_projects': completed_projects,
        'in_progress_projects': in_progress_projects
    })

@login_required
def profile(request):
    return render(request, 'profile.html')

@login_required
def project_list(request):
    projects = Project.objects.filter(project_leader=request.user)
    return render(request, 'project_list.html', {'projects': projects})

@login_required
def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'project_detail.html', {'project': project})

@login_required
def new_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'new_project.html', {'form': form})

@login_required
def project_create(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.project_leader = request.user
            project.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'project_form.html', {'form': form})

@login_required
def project_edit(request, pk):
    project = Project.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm(instance=project)
    return render(request, 'templates/project_form.html', {'form': form})

@login_required
def project_delete(request, pk):
    project = Project.objects.get(pk=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('project_list')
    return render(request, 'templates/project_confirm_delete.html', {'project': project})
