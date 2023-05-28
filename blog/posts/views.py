from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
# Create your views here.


def index(request):
    models = Post.objects.all()
    print(models)
    return render(request,'index.html',{"posts":models})

def post(request,pk):
    print("pk value is ",pk)
    post = Post.objects.get(id=pk)
    print(post)
    return render(request,'posts.html',{"posts":post})

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')
        else:
            messages.info(request,"Invalide Credentials")
            return redirect('/')

    else:
        return render(request,'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        if User.objects.filter(username=username).exists():
            messages.info(request,"User Name is alreay taken")
            return redirect("register")
        elif User.objects.filter(email=email).exists():
            messages.info(request,"Email is alreay taken")
            return redirect("register")
        else:
            user=User(username=username,email=email,password=password)
            user.save()
            return redirect('/')
    else:
        return render(request,'register.html')
