from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegisterForm, TaskForm  # Add TaskForm
from .models import Task  # Add Task model

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        username = request.POST.get('username')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, f'Username "{username}" already exists. Please choose another username.')
            return render(request, 'registration/register.html', {'form': form})
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('task_list')
        else:
            return render(request, 'registration/register.html', {'form': form})
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    
    completed_tasks = tasks.filter(completed=True)
    pending_tasks = tasks.filter(completed=False)
    
    total_tasks = tasks.count()
    completed_count = completed_tasks.count()
    pending_count = pending_tasks.count()
    
    context = {
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
        'total_tasks': total_tasks,
        'completed_count': completed_count,
        'pending_count': pending_count,
    }
    return render(request, 'todo/task_list.html', context)

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'Task created successfully!')
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'todo/task_form.html', {'form': form, 'action': 'Create'})

@login_required
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully!')
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todo/task_form.html', {'form': form, 'action': 'Update'})

@login_required
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted successfully!')
        return redirect('task_list')
    return render(request, 'todo/task_confirm_delete.html', {'task': task})

@login_required
def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.completed = not task.completed
    task.save()
    messages.success(request, f'Task marked as {"completed" if task.completed else "pending"}!')
    return redirect('task_list')