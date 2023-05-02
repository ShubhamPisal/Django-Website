from django.urls import path
from blog import views
# from django.contrib.auth import views as auth_views


#We need to add urls as we created the views in app & templet to see it in webpage
urlpatterns = [
    path('', views.home, name='blog-homePage'),
    path('Login', views.loginUser, name='blog-LoginPage'),
    path('Logout', views.logoutUser, name='blog-Logout'),
    path('ForgetPassword', views.forgetpassword, name='blog-ForgetPasswordPage'),
    path('SignUp/', views.signup, name='blog-SignUpPage'),
    path('Todo', views.TodoList, name='blog-TodoPage'),
    path('update/<int:sno>', views.Todoupdate, name='blog-TodoupdatePage'),
    path('delete/<int:sno>', views.Tododelete, name='blog-TododeletePage'),
    path('Chats', views.Chats, name='blog-ChatsPage'),
    path('profile/', views.profile, name='blog-profilePage'),
    path('chatmenu/', views.chatmenu, name='blog-chatmenuPage'),

]
