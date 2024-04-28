from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import TodoItem
from .forms import TodoItemForm

def todo_list(request):
    todos = TodoItem.objects.all()
    return render(request, 'todo/todo_list.html', {'todos': todos})

def todo_create(request):
    if request.method == 'POST':
        form = TodoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')
    else:
        form = TodoItemForm()
    return render(request, 'todo/todo_create.html', {'form': form})

def todo_update(request, todo_id):
    todo = get_object_or_404(TodoItem, id=todo_id)
    if request.method == 'POST':
        form = TodoItemForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('management_view')
    else:
        form = TodoItemForm(instance=todo)
    return render(request, 'todo/todo_update.html', {'form': form, 'todo': todo})

def todo_delete(request, todo_id):
    todo = get_object_or_404(TodoItem, id=todo_id)
    if request.method == 'POST':
        todo.delete()
        return redirect('management_view')
    return render(request, 'todo/todo_delete.html', {'todo': todo})
    
def management_view(request):
    todos = TodoItem.objects.all()
    return render(request, 'todo/todo_management.html', {'todos': todos})

def toggle_completion(request, todo_id):
    try:
        todo = TodoItem.objects.get(id=todo_id)
        todo.completed = not todo.completed
        todo.save()
        return JsonResponse({'completed': todo.completed, 'completion_status_icon': todo.completion_status_icon})
    except TodoItem.DoesNotExist:
        return JsonResponse({'error': 'Todo not found'}, status=404)