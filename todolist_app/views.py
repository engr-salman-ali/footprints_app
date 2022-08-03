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
from django.http import HttpResponseRedirect

def index(request):
    contenxt = {'welcome_text':"Welcome to FootPrints your home to manage your tasks"}
    return render(request,'todolist/index.html', contenxt)

# The decoraator login required is used as it authenticates if the user is authorized to access functionality
@login_required
def todolist(request):
    """Here we recive task post request from the user and validate it against 
    specified values
     -once we get through it we redirect to the task page again with response 3XX
     -else we display message object to enter a valid task
     -Since we have added all the tasks on single page , we do not need separate GET method for any task
    """
    if request.method == "POST":
        form = TodoForm(request.POST or None)
        if form.is_valid():
            instance  = form.save(commit=False)
            instance.owner = request.user
            instance.save()
            messages.success(request , ("Task Added Successfully!"))
        else:
            messages.error(request , ("Please Enter A valid task"))
        return redirect('todolist')
    else:
        all_tasks = TodoList.objects.all().order_by('-updated','created').filter(owner= request.user)
        paginator = Paginator(all_tasks,10)
        page = request.GET.get('page')
        all_tasks = paginator.get_page(page)
        return render(request,'todolist/todolist.html', {'all_tasks':all_tasks})

@login_required
def delete_task(request,task_id):
    """
    Here recived a delete request from the user , 
    try- to check if the object exist or user is trying to redelete access the deleted task
    except- the task is already deleted or does not exit
    else- once we find the task we can delete it
    """
    try:
        task = TodoList.objects.get(pk=task_id)
    except(TodoList.DoesNotExist):
        messages.error(request , ("Task already deleted"))
    else:
        if task.owner == request.user :
            task.delete()
        else:
            messages.error(request , ("Only owner can delete the task!"))
    
    return redirect('todolist')

@login_required
def update_task(request, task_id):
    """
    Here we recive update request from the user ,
    if the request method is post 
    """
    if request.method == "POST":
        try:
            task = TodoList.objects.get(pk=task_id)
            form = TodoForm(request.POST or None, instance=task)
            if form.is_valid():
                form.save()
            messages.success(request , ("Task Updated"))
            return redirect('todolist')
        except((TodoList.DoesNotExist)):
            messages.error(request , ("The task does not exist"))
            return redirect('todolist')
    else:
        """if user tries to update a task that does not exist ,
        we redirect them to task list with message"""
        try:
            task_to_update = TodoList.objects.get(pk=task_id)

        except(TodoList.DoesNotExist):
            messages.error(request , ("The task you are trying to acess does not exist"))
            return redirect('todolist')

        return render(request,'todolist/update.html', {'task_to_update':task_to_update})




def contactUs(request):
    contenxt = {'contact_text':"Welcome to Contact Page"}
    return render(request,'todolist/contactus.html', contenxt)



def aboutUs(request):
    contenxt = {'about_text':"Welcome to About Us"}
    return render(request,'todolist/aboutus.html', contenxt)
