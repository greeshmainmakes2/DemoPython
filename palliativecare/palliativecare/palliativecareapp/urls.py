
from django.urls import path
from . import views
urlpatterns = [
    path('',views.display,name='display'),

    # path('home/',views.home,name='home'),
    # path('home/operations/',views.operations,name='operations'),
]