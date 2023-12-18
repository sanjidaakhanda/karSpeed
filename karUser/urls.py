from django.urls import path
from . import views

urlpatterns = [
   
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name = 'login'),
    path('logout/',views.user_logout,name='logout'),
    path('about/',views.about,name= 'about'),
    path('update/',views.profileUpdate,name = 'update'),
    path('password/',views.password_change, name = 'password')
]
