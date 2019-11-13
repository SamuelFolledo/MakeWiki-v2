from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from wiki.models import Page


from django.contrib.auth.forms import UserCreationForm #for signup
from django.urls import reverse_lazy #for signup
from django.views.generic import CreateView #for signup

class SignUpView(CreateView): #for signup
    form_class = UserCreationForm #for signup
    success_url = reverse_lazy('login') #for signup, login because signup is just creating account, so we take them to the login page. #reverse_lazy = it's going to reverse engineer the url from the url_pattern name field (login, which is /accounts/login). It waits until we actually use success_url
    template_name = 'signup.html' #for signup


class PageListView(ListView):
    """ Renders a list of all Pages. """
    model = Page

    def get(self, request):
        """ GET a list of Pages. """
        pages = self.get_queryset().all()
        return render(request, 'list.html', {
          'pages': pages
        })

class PageDetailView(DetailView):
    """ Renders a specific page based on it's slug."""
    model = Page

    def get(self, request, slug):
        """ Returns a specific wiki page by slug. """
        page = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'page.html', {
          'page': page
        })
