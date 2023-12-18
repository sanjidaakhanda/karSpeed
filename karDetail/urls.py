from django.urls import path
from . import views

urlpatterns = [
   
    # path('detail/',views.add_car,name='detail'),
    path("detail/",views.AddCarCreateView.as_view(),name = 'detail'),
    path("view/<int:id>/",views.CarDetailView.as_view(),name = 'view_all'),
    

    
    ]