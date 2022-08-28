from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Project, Tag
from .forms import ProjectForm, ReviewForm
from .utils import searchProjects, paginateProjects
# Create your views here.

def home(request):
    # return HttpResponse('I have updated the content')
    return render(request, 'projects.html')

def projects(request):
    projects, search_query = searchProjects(request)

    custom_range , projects = paginateProjects(request, projects, 5)



    context = {'projects':projects,"search_query":search_query,'custom_range':custom_range}
    return render(request, 'project/projects.html',context)

def single_project(request,pk):
    singleObj = Project.objects.get(id=pk)
    form      = ReviewForm()

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = singleObj
        review.owner  = request.user.profile
        review.save()

        singleObj.getVoteCount
        
        # Update project vote count 
        messages.success(request, 'Your review was successfully submitted!')
        return redirect('single_project', pk=singleObj.id)


    return render(request,'project/single-project.html',{'projectObj':singleObj, 'form':form})

@login_required(login_url="login")
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
             project = form.save(commit=False)
             project.owner = profile
             project.save()
             return redirect('account')
    
    context = {'form':form}
    return render(request,"project/project_form.html",context)


@login_required(login_url="login")
def updateProject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form    = ProjectForm(instance=project) 
    if request.method == 'POST':
        form = ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid():
            form.save()
            return redirect('account')
    context = {'form': form }
    return render(request,'project/project_form.html',context)

@login_required(login_url="login")
def deleteProject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
    context = {'object': project }
    return render(request,'delete_template.html',context)
    

