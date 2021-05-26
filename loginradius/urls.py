

from django.urls import path
from . import views
urlpatterns = [
    path("",views.login,name="login"),
    path("dashboard",views.dahboard,name="dashboard"),
    path("<str:action>/auth",views.auth,name="auth"),
    
]

