from django.urls import path
from .views.contact_view import ContactView
from .views.login_view import LoginView, LogoutView
from .views.user_preferences_view import user_preferences
from .views.register_view import RegisterView

app_name = "users"

urlpatterns = [
  path('register/', RegisterView.as_view(), name='register'),
  path("login/", LoginView.as_view(), name="login"),
  path("logout/", LogoutView.as_view(), name="logout"),
  path("user_preferences/", user_preferences, name="user_preferences"),
  path("contact/", ContactView.as_view(), name="contact"),
]

