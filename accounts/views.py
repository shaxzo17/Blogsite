from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login , logout , authenticate
# Create your views here.

def singnup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        last_name = request.POST['last_name']
        first_name = request.POST['first_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request , 'Xato password')
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request , 'Bu username allaqachon bor')
            return redirect('signup')

        User.objects.create_user(username=username , first_name=first_name , last_name=last_name ,email=email ,
                                        password=password1)
        messages.success(request , 'Royxattan ottiz')

        return redirect('login')
    return render(request , 'account/signup.html' )

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        if not username or not password:
            messages.error(request, 'Login yoki parol kiritilmadi')
            return redirect('login')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Siz login qildingiz')
            return redirect('main')
        else:
            messages.error(request, 'Login yoki parol noto‘g‘ri')
            return redirect('login')

    return render(request, 'account/login.html')

def logout_view(request):
    logout(request)
    messages.error(request ,'Siz dasturdan chiqdingiz')
    return redirect('main')