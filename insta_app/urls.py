from django.urls import path

from . import views

urlpatterns = [
    path("", views.hello, name="hello"),
    path('<int:id>/', views.detail, name='detail'),
    path('login', views.login, name='Login'),
    path('signup', views.signup, name='Signup')
]