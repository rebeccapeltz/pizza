from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
# from users.forms import SignUpForm


from django.contrib.auth.models import User



# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {"message": None})
    context = {
        "user": request.user
    }
    return render(request, "users/user.html", context)

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("menu"))
    else:
        return render(request, "users/login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {"message": "Logged out."})

def register_view(request):
    return render(request, "users/register.html")

    
def process_register_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    email = request.POST["email"]
    firstname = request.POST["firstname"]
    lastname = request.POST["lastname"]


    if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
        user = User.objects.create_user(username, email, password)
        user.first_name = firstname
        user.last_name = lastname
        user.save()
        test = authenticate(username = username, password = password)
        login(request, user)
        return render(request, "users/user.html", {"message": "Registration complete."})
    # else:
    #     raise forms.ValidationError('Looks like a username with that email or password already exists')

    # user = User(username=username, password=password, email=email,first_name=firstname, last_name=lastname)
    # user.save()
    return render(request, "users/login.html", {"message": "Problem registering. Username or email in use"})

#no such table: main.auth_user__old

