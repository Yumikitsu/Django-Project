from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib import messages
from .models import RegisteredUser
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin

def app_homepage(request):
    try:
        if usrnme:
            userdetails = {'username': usrnme}
            return render(request, "loggedin.html", userdetails)
    except NameError:
        return render(request, 'homepage.html')

def about_us(request):
    try:
        if usrnme:
            return render(request, "aboutUs.html")
    except NameError:
        return render(request, "aboutUs.html")

def services(request):
    try:
        if usrnme:
            return render(request, "services.html")
    except NameError:
        return render(request, "services.html")

def contact_us(request):
    try:
        if usrnme:
            return render(request, "contactUs.html")
    except NameError:
        return render(request, "contactUs.html")

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully")
            return redirect("signin")
    else:
        form = RegisterForm()
        user_info = {'form': form}
        return render(request, "register.html", user_info)

def signin(request):
    global usrnme
    if request.method == 'POST':
        usrnme = request.POST['username']
        psswrd = request.POST['pswd']

        try:
            user = RegisteredUser.objects.get(name=usrnme)
            if usrnme == user.name and psswrd == user.password:
                return redirect("loggedin")
            else:
                messages.info(request, "Incorrect password")
                return redirect("signin")
        except ObjectDoesNotExist:
            messages.info(request, "The user does not exist")
            return redirect("signin")
    else:
        return render(request, "signin.html")
    
def loggedin(request):
    image_file = RegisteredUser.objects.get(name=usrnme)

    pic_path = str(image_file.profilePic)
    full_pic_path = 'media/' + pic_path
    userdetails = {'username': usrnme, 'image': full_pic_path}
    return render(request, "loggedin.html", userdetails)

def logout(request):
    global usrnme
    del usrnme
    return render(request, "logout.html")

class UserListView(ListView):
    model = RegisteredUser
    template_name = "user_data.html"
    context_object_name = 'alldata'

class UserDetailView(DetailView):
    model = RegisteredUser

class UserCreateView(CreateView):
    model = RegisteredUser
    form_class = RegisterForm

class UserUpdateView(UserPassesTestMixin, UpdateView):
    model = RegisteredUser
    form_class = RegisterForm

    def test_func(self):
        if self.request.user.is_active:
            return True
        else: return False

class UserDeleteView(UserPassesTestMixin, DeleteView):
    model = RegisteredUser
    success_url = '/userlist'

    def test_func(self):
        if self.request.user.is_active:
            print(self.request.user)
            return True
        else: return False