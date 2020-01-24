from django.urls import path

from . import views

urlpatterns = [
    path('/login', views.login, name='login'),
    path('/register', views.register, name='register'),
    path('/', views.profile_account, name='profile-account'),
    path('/change-password', views.change_password, name='change_password'),
    path('/myproperties', views.myproperties, name='myproperties'),
    path('/test', views.test, name='test'),

]
