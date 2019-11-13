

from django.contrib.auth.forms import UserCreationForm #for signup
from django.urls import reverse_lazy #for signup
from django.views.generic import CreateView #for signup

class SignUpView(CreateView): #for signup
    form_class = UserCreationForm #for signup
    success_url = reverse_lazy('login') #for signup, login because signup is just creating account, so we take them to the login page. #reverse_lazy = it's going to reverse engineer the url from the url_pattern name field (login, which is /accounts/login). It waits until we actually use success_url
    template_name = 'registration/signup.html' #for signup
