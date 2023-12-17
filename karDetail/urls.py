from django.urls import path
from . import views

urlpatterns = [
   
    path('detail/',views.add_car,name='detail'),
    path("view/<int:id>/",views.CarDetailView.as_view(),name = 'view_all'),
    # path('login/',views.user_login,name = 'login'),
    # path('detail/<int:id>/', views.carDetail, name='detail')

    
    ]