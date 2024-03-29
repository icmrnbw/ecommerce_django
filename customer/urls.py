from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login_user/', views.login_view, name='login'),
    path('logout_user/', views.logout_view, name='logout'),
    path('contact/', views.contact_view, name='contact'),
    # path('email-sub/', views.email_sub, name='email_sub'),
]
