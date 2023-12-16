from django.urls import path
from . import views

urlpatterns = [
    path("",views.main,name = 'Home'),
    path("about/",views.about, name ="About"),
    path('register/', views.sign_up, name = 'Register'),
    path('login/',views.sign_in, name = 'Login'),
    path('profile/',views.profile, name = 'Profile'),
    path('logout/',views.logout_user, name = 'Logout'),
    path('adoption/',views.adoption, name = 'Adoption')
]
