import datetime
from django.shortcuts import render
from .models import Todo

def index(request):
    date = datetime.datetime.now()
    todos = Todo.objects.filter(owner=request.user)
    context = {
        "date": date, 
        "todos": todos,
    }
    return render(request, 'todos/index.html', context)