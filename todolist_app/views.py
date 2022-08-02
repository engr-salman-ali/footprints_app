from wsgiref.util import request_uri
from django.shortcuts import render , redirect
from django.http import HttpResponse
from todolist_app.models import TodoList
from todolist_app.forms import TodoForm
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def index(request):
    contenxt = {'welcome_text':"Welcome to FootPrints your home to manage your tasks"}
    return render(request,'todolist/index.html', contenxt)

@login_required
def todolist(request):
    if request.method == "POST":
        form = TodoForm(request.POST or None)
        if form.is_valid():
            instance  = form.save(commit=False)
            instance.owner = request.user
            instance.save()
        messages.success(request , ("Task Added Successfully!"))
        return redirect('todolist')
    else:
     
        all_tasks = TodoList.objects.all().order_by('-updated','created').filter(owner= request.user)
        paginator = Paginator(all_tasks,10)
        page = request.GET.get('page')
        all_tasks = paginator.get_page(page)
        return render(request,'todolist/todolist.html', {'all_tasks':all_tasks})

@login_required
def delete_task(request,task_id):
    task = TodoList.objects.get(pk=task_id)
    if task.owner == request.user :
        task.delete()
    else:
        messages.error(request , ("Only owner can delete the task!"))
    
    return redirect('todolist')

@login_required
def update_task(request, task_id):
    if request.method == "POST":
        task = TodoList.objects.get(pk=task_id)
        form = TodoForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
        messages.success(request , ("Task Updated"))
        return redirect('todolist')
    else:
        task_to_update = TodoList.objects.get(pk=task_id)
        return render(request,'todolist/update.html', {'task_to_update':task_to_update})




def contactUs(request):
    contenxt = {'contact_text':"Welcome to Contact Page"}
    return render(request,'todolist/contactus.html', contenxt)



def aboutUs(request):
    contenxt = {'about_text':"Welcome to About Us"}
    return render(request,'todolist/aboutus.html', contenxt)
