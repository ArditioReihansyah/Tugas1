from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from todolist.models import Task
from todolist.forms import TaskForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    task_list = Task.objects.filter(user= request.user)
    context = {
        'task_list' : task_list,
        'username' : request.user.username,
    }
    return render(request, "todolist.html", context)

def delete_task(request, id):
    task_list = Task.objects.filter(id=id)
    task_list.delete()
    return redirect('todolist:show_todolist')

def update_task(request, id):
    task_list = Task.objects.filter(id=id)
    task = task_list[0]
    task.is_finished = not task.is_finished
    task.save()
    return redirect('todolist:show_todolist')

def create_task(request):
    form = TaskForm()
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.user = request.user
            form.save()
            return redirect('todolist:show_todolist')
        else:
            form = TaskForm()
    context = {'form': form}
    return render(request, 'create-task.html', context)


def registrasi(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'registrasi.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')