from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User,auth
from django.contrib import messages
from . models import todo


def index(request):
    return render(request,'index.html')


def create_todo(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        new_todo = todo(user=request.user, title=task)
        new_todo.save()
        messages.success(request, "Task has been added successfully.")
        return redirect('create_todo')  # Redirect to the same page to display the updated task list.

    all_todos = todo.objects.filter(user=request.user)
    
    context = {
        'todos': all_todos
    }
    return render(request, 'todo.html', context)


def register(request):
    if request.method =='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.info(request,"username already exist")
            return redirect('register')
        elif User.objects.filter(email=email).exists():
             messages.info(request,"email already exist")
             return redirect('register')
        else:
         user=User.objects.create_user(username=username,email=email,password=password)
         user.save()
        return redirect('/login')
    else:
        return render(request,'register.html')

def loginn(request):
    if request.method =='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/todo')
        
        else:
            messages.info(request, "Invalid Login")
            return redirect('login')

    return render(request,'login.html')



# views.py



def delete_todo(request, todo_id):
    todo_object = get_object_or_404(todo, id=todo_id, user=request.user)
    todo_object.delete()
    messages.success(request, "Task has been deleted successfully.")
    return redirect('create_todo')

def finish_todo(request, todo_id):
    todo_object = get_object_or_404(todo, id=todo_id, user=request.user)
    todo_object.complete = True
    todo_object.save()
    messages.success(request, "Task has been marked as finished.")
    return redirect('create_todo')


def logout(request):
    auth.logout(request)
    return redirect('/')