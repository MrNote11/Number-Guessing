from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='game/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('hint/', views.home, name='hint'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('submit_feedback/', views.submit_feedback, name='submit_feedback'),
]
