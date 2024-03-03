from django.shortcuts import render, redirect
from .models import TodoItem

def todo_list(request):
    todos = TodoItem.objects.all()
    return render(request, 'todo_app/todo_list.html', {'todos': todos})

def todo_create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        TodoItem.objects.create(title=title)
        return redirect('todo_list')
    return render(request, 'todo_app/todo_create.html')

def todo_update(request, todo_id):
    todo = TodoItem.objects.get(id=todo_id)
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.completed = request.POST.get('completed') == 'on'
        todo.save()
        return redirect('todo_list')
    return render(request, 'todo_app/todo_update.html', {'todo': todo})

def todo_delete(request, todo_id):
    todo = TodoItem.objects.get(id=todo_id)
    if request.method == 'POST':
        todo.delete()
        return redirect('todo_list')
    return render(request, 'todo_app/todo_delete.html', {'todo': todo})