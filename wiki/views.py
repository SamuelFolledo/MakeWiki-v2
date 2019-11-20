from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views import View #for create page view

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from wiki.models import Page
from wiki.forms import CreatePageForm

class PageCreateView(View):
    model = Page
    def get(self, request):
        # Code block for GET request
        form = CreatePageForm()
        context = { 'form':form }
        return render(request, 'create.html', context)
    def post(self, request):
        # Code block for POST request
        form = CreatePageForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            page = form.save()
            # form.save()
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect(reverse_lazy('wiki:wiki-details-page', args=[page.title])) #wiki is the app name and wiki-details-page is the name in urls.py
        return render(request, 'create.html', {'form': form})

# def new_page(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = CreatePageForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/thanks/')

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = CreatePageForm()

#     return render(request, 'create.html', {'form': form})
    

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
