from django.urls import path
from accounts.views import user_login, user_signup


urlpatterns = [
    path("signup/", user_signup, name="signup"),
    path("login/", user_login, name="login"),
]
