from django.urls import path
from .views.contact_view import ContactView
from .views.login_view import LoginView, LogoutView
from .views.user_preferences_view import user_preferences
from .views.register_view import RegisterView
from .views.profile_view import ProfileDetailView, ProfileUpdateView

app_name = "users"

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("profile/<pk>/", ProfileDetailView.as_view(), name="profile_detail"),
    path("profile/update/<pk>/", ProfileUpdateView.as_view(), name="profile_update"),
    path("user_preferences/", user_preferences, name="user_preferences"),
]
