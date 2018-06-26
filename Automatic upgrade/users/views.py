# from django.contrib.auth import authenticate, login, hashers
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
# from django.shortcuts import render,HttpResponse
# from django.views.generic import View
# from django.contrib.auth.hashers import make_password
# import json
#
# from .forms import LoginForm, RegisterForm,ForgetForm,ChangeForm,UploadImageForm
from .models import UserProfile
#
#
# # Create your views here.
#
# #
class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username)|Q(email=username)|Q(nick_name=username))
            if user.check_password(password):
                return user
            return None

        except Exception as e :
            print(e)
            return None

