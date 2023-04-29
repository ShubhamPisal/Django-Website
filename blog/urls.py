from django.urls import path
from blog import views
from django.conf import settings
from django.conf.urls.static import static
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
    path('message', views.message, name='blog-messagePage'),
    path('Chats', views.Chats, name='blog-ChatsPage'),
    path('profile/', views.profile, name='blog-profilePage'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)