
from django.urls import path
from . import views
urlpatterns = [
    path('register',views.register_home,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),

    path('registertemp',views.registertemp,name='registertemp'),
    path('logintemp',views.logintemp,name='logintemp')
    ]