from . import views
from django.urls import path
from django.views.generic.base import TemplateView 
from django.contrib.auth import views as auth
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.hello, name='hello'),
    path('<int:id>/', views.detail, name='detail'),
    path('login', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('signup', views.signup, name='signup')
]