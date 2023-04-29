from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout, authenticate, login
# from django.contrib.auth.decorators import login_required
from blog.forms import NewUserForm 
from blog.models import Todo,Messages
from django.contrib import messages
import random
import string


# Create the home page view
def home(request):
    return render(request, 'Home.html')

#Created to generate random string for the cptcha
def string_generator(): 
    rand_string = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    global random_string
    random_string = rand_string
    return random_string

# Create the login page view
def loginUser(request):
          
    if request.method=='POST':
        #collect user input after submitting form
        username = request.POST.get('username')
        Epassword = request.POST.get('password')
        Captcha = request.POST.get('Captcha')

        password = bytes([eval(i)-10 for i in Epassword.split(',')]).decode('utf8')

        #print(username,password,Captcha) # used to verify the inpunt provided in the frount end is correct for backend
        if Captcha == random_string: #Compare generated string with user input
        # check if user has entered correct credentials
            user = authenticate(username=username, password=password)
            if user is not None:
                # A backend authenticated the credentials
                login(request, user)
                return redirect('/Todo')
            else:
                # No backend authenticated the credentials
                messages.warning(request, 'Enter Correct Password!')
                return render(request, 'Login.html', {'cap': random_string , 'enablecaptcha':0})
        else:
            messages.warning(request, 'Enter Correct Captch!')
   
    string_generator() #To refresh captch when page is refreshed
    # print(random_string) # used when captcha is not displaying on page
    return render(request, 'Login.html', {'cap': random_string , 'enablecaptcha':0})

# Create the logout page view
def logoutUser(request):
    logout(request)
    return redirect('blog-LoginPage')
   
# Create the forgetpassword page view
def forgetpassword(request):
    return render(request, 'ForgetPassword.html')

# Create the signup page view
def signup(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully for {username}!' )
            return redirect('blog-homePage')
    else:
        form = NewUserForm()
    return render (request, 'SignUp.html',{'form' : form})

# Create the ToDo page view
def TodoList (request):
    if request.user.is_anonymous:
        return redirect('/Login')
    else:
        context = {
          'tasks' : Todo.objects.all()
        }
        if request.method=='POST':
            title = request.POST.get('title')
            desc = request.POST.get('desc')
            content=Todo(title=title,desc=desc)
            content.save()
            return redirect('/Todo')
        return render(request, 'Todo.html', context)

# Create the ToDoUpdate page view
def Todoupdate(request,sno):
    
    if request.method=='POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        content=Todo(sno=sno ,title=title ,desc=desc)
        content.save()
        return redirect('/Todo')
        
    context = {
        'todo' : Todo.objects.filter(sno=sno).first()
    }
    return render(request,'update.html', context)

# Create the ToDo Delete record view
def Tododelete(request,sno):
    content=Todo.objects.get(sno=sno)
    content.delete()
    return redirect('/Todo')

# Create the message sent view
def message(request):
    if request.method=='POST':
        message = request.POST.get('message')
        content=Messages(message=message)
        content.save()
        return redirect('/Chats')
    return render(request, '404.html')

# Create the Chats record view
def Chats(request):
    if request.user.is_anonymous:
        return redirect('/Login') 
    context = {
        'Conversions' : Messages.objects.all() 
    }
    return render(request, 'message.html', context)

def profile(request):
    return render(request, 'profile.html')


#added for post # Not tested or tryed yet
# from django.shortcuts import render
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.views.generic import (
#     ListView,
#     DetailView,
#     CreateView,
#     UpdateView,
#     DeleteView
# )
# from .models import Post


# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }
#     return render(request, 'blog/home.html', context)


# class PostListView(ListView):
#     model = Post
#     template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
#     context_object_name = 'posts'
#     ordering = ['-date_posted']


# class PostDetailView(DetailView):
#     model = Post


# class PostCreateView(LoginRequiredMixin, CreateView):
#     model = Post
#     fields = ['title', 'content']

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)


# class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Post
#     fields = ['title', 'content']

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

#     def test_func(self):
#         post = self.get_object()
#         if self.request.user == post.author:
#             return True
#         return False


# class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = Post
#     success_url = '/'

#     def test_func(self):
#         post = self.get_object()
#         if self.request.user == post.author:
#             return True
#         return False