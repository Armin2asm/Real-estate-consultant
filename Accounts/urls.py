from django.urls import path
from .views import ContactView, SignUpView
from django.contrib.auth.views import LoginView, LogoutView

app_name = "account"

urlpatterns = [
    path("contact/", ContactView.as_view(), name="contact"),


    path( "login/", LoginView.as_view(template_name="Accounts/login.html"),    name="login"  ),

    path(    "logout/",    LogoutView.as_view(next_page="Home"),    name="logout"),
    path(    "signup/",    SignUpView.as_view(),    name="signup"),
    ]