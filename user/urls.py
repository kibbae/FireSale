from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='user'),
    path('register', views.register, name='register'),
    path('login', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout', Logoutview.as_view(next_page='login'), name='logout')
]