from django.urls import path
from . import views


urlpatterns = [
    path("",views.main,name = 'Home'),
    path("about/",views.about, name ="About"),
    path('register/', views.register, name = 'Register' )
]