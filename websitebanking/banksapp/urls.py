from . import views
from django.urls import path
app_name='banksapp'
urlpatterns=[
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('personaldet',views.personaldet,name='personaldet'),
    path('success',views.success,name='success'),

]
