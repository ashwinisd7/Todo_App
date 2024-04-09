from django.shortcuts import render, redirect
from .models import ToDoItem
from .forms import ToDoItemForm

'''def index(request):
    # Add your view logic here
    return render(request, 'demoapp/index.html', context={})

def create_todo_item(request):
    if request.method == 'POST':
        form = ToDoItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_list')  # Redirect to the to-do list page
    else:
        form = ToDoItemForm()
    return render(request, 'create_todo_item.html', {'form': form})'''

def index(request):
    tasks = ToDoItem.objects.all()
    form = ToDoItemForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirect to the same page after form submission
    return render(request, 'demoapp/index.html', {'tasks': tasks, 'form': form})
