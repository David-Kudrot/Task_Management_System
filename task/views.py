from django.shortcuts import render, redirect , get_object_or_404
from task.forms import TaskForm
from task.models import TaskModel

# Create your views here.

def add_task(request):
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('add_task')
    else:
        task_form = TaskForm()
    
    return render(request, 'task.html', {'form': task_form})


def show_task(request):
    tasks = TaskModel.objects.all()
    return render(request, 'show_task.html', {'tasks': tasks})




def edit_task(request, id):
    task = get_object_or_404(TaskModel, pk=id)
    tasks = TaskModel.objects.all()
    if request.method == 'POST':
        task_form = TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return render(request, 'show_task.html', {'tasks': tasks})
    else:
        task_form = TaskForm(instance=task)
    
    return render(request, 'task.html', {'form': task_form})

    
def delete_task(request, id):
    task = TaskModel.objects.get(pk=id)
    task.delete()
    return redirect('show_task')
    