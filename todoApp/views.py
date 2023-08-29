from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, TodoForm
from django.contrib import messages
from .models import Todo


# Create your views here.
def index(request):
    return render(request, "index.html")


def register_user(request):
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        name = request.POST.get("name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if password1 != password2:
            messages.error(request, "Password does not match")
            print("pwd error")
            return render(request, "login.html")
        else:
            if form.is_valid():
                form.save()
                print("done user")
                messages.success(request, "User registered successfully!")
                return render(request, "login.html")

    context = {
        "form": form,
    }
    return render(request, "register.html", context)


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "You have been logged in successfully.")
            return redirect("index")

        else:
            return JsonResponse(
                {"status": "error", "message": "Invalid username or password."}
            )
    return render(request, "login.html")


def logout_user(request):
    logout(request)
    messages.add_message(
        request, messages.SUCCESS, "You have been logged out successfully."
    )
    return redirect("index")


@login_required(login_url="/login")
def add_todo(request):
    form = TodoForm()
    tododata = Todo.objects.filter(host=request.user)
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.host = request.user
            form.save()
            messages.success(request, "Todo added successfully")
            return redirect("add_todo")
    return render(request, "todo.html", {"form": form, "tododata": tododata})


@login_required(login_url="/login")
def update_todo(request, pk):
    todo = Todo.objects.get(id=pk)
    form = TodoForm(instance=todo)
    print(request.user)
    print(todo.host)
    if request.user != todo.host:
        return HttpResponse("You are not allowed to here...")

    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, "Todo updated successfully")
            return redirect("add_todo")
    return render(request, "update_todo.html", {"form": form})


@login_required(login_url="/login")
def delete_todo(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.user != Todo.host:
        return HttpResponse("You are not allowed to here...")

    todo.delete()
    messages.success(request, "Todo deleted successfully")
    return redirect("add_todo")
