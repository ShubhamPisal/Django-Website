from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import logout, authenticate, login
# from django.contrib.auth.decorators import login_required
from blog.forms import NewUserForm 
from blog.models import Todo
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
        password = request.POST.get('password')
        Captcha = request.POST.get('Captcha')

        # print(username,password,Captcha) # used to verify the inpunt provided in the frount end is correct for backend

        if Captcha == random_string: #Compare generated string with user input

        # check if user has entered correct credentials
            user = authenticate(username=username, password=password)
            if user is not None:
                # A backend authenticated the credentials
                login(request, user)
                return redirect('/Logedin')

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

# Create the logedin page view
def logedin(request):
    if request.user.is_anonymous:
         return redirect('/Login') 
    return render(request, 'Logedin.html')

# Create the ToDo page view
def TodoList (request):
    context = {
        'tasks' : Todo.objects.all() 
    }
    if request.method=='POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        print(title,desc)
        content=Todo(title=title,desc=desc)
        content.save()
        return redirect('/Todo')
        
    return render(request, 'Todo.html', context)

# Create the ToDoUpdate page view
def Todoupdate(request,sno):
    context = {
        'tasks' : Todo.objects.filter(sno=sno).first()
    }
    if request.method=='POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        content=Todo(title=title,desc=desc)
        content.save()
        return redirect("/Todo")
        
    todo = Todo.objects.filter(sno=sno).first()
    print(sno)
    print(todo)
    print(context)
    return render(request,'update.html', context)

# Create the ToDo Delete record view
def Tododelete(sno):
    todo = Todo.objects.filter(sno=sno).first()
    return redirect("/Todo")