from django.urls import path
from AuthorLoginApp import views

app_name = 'AuthorLoginApp'

urlpatterns = [
    path('author_signup/', views.signup_view, name='signup'),
    path('author_login/', views.login_view, name='login'),
    path('author_logout/', views.logout_view, name='logout'),
    path('change_password/', views.change_password_view, name='password'),
    path('change_email/', views.change_email, name='email'),
]