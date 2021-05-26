from django.shortcuts import redirect, render
from django.http import HttpResponse
from .lr import loginradius
from django.views.generic.base import RedirectView

# Create your views here.
def login(request):
     return render(request,"loginradius/index.html",{
     })
def dahboard(request):
      return render(request,"loginradius/dashboard.html",{
          })

def auth(request,action):
     if action=="register":
          return render(request,"loginradius/auth.html",{
               "msg":"Registration Sucessfull You can login now"
          })
     elif action=="login":
          return render(request,"loginradius/auth.html",{

               "msg":"login Sucessfull"
          })
     elif action=="fp":
          return render(request,"loginradius/auth.html",{
              
          })
     elif action=="logout":
          return render(request,"loginradius/auth.html",{
               "msg":"logout Sucessfull"
          })
     else: 
          return HttpResponse("Invalid URL")
          