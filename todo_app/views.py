from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import User_Tasks,completed_tasks
# Create your views here.

def index(request):
  tasks=User_Tasks.objects.all()
  done_tasks=completed_tasks.objects.all()
  return render(request,"todo/tasks.html",{"tasks":tasks,"done_tasks":done_tasks})

def store_data(request):
  if request.method=="POST":
    data=request.POST.get("data")
    User_Tasks.objects.create(data=data)
  return redirect('index')

def completed(request,task_id):
  task=User_Tasks.objects.get(id=task_id)
  if request.method=="POST":
    action=request.POST.get("action")
    if action=="completed":
      completed_tasks.objects.create(data=task)
      task.delete()
    else:
       return redirect('task_id/edit_task')
  return redirect('index')

def delete_task(request,delete_id):
  task=completed_tasks.objects.get(id=delete_id)
  task.delete()
  return redirect("index")

def edit_task(request,task_id):
  task=get_object_or_404(User_Tasks,id=task_id)
  return render(request,'todo/edit_task.html',{"task":task})

def update(request,task_id):
  t=User_Tasks.objects.get(id=task_id)
  if request.method=="POST":
    action=request.POST.get("action")

    if action=="update":
      t.data=request.POST.get("updated_data")
      t.save()
    else:
      t.delete()  
  return redirect('index')