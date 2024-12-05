from django.urls import path
from . import views  # Import your app's views module
urlpatterns = [
    path('', views.RegisterView, name='register'),
    path('login', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('refresh_token/<int:id>/', views.generate_tokens_for_all_users, name='refresh_token'),
    path('user_details', views.user_details, name='user_details'),
    path('client_dashboard',views.client_dashboard,name='client_dashboard'),
    path('moderator_dashboard',views.moderator_dashboard,name='moderator_dashboard'),
]