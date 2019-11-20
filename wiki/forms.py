from django import forms
from wiki.models import Page


class PageForm(forms.ModelForm):
    """ Render and process a form based on the Page model. """
    model = Page

class CreatePageForm(forms.ModelForm):
    # page_title = forms.CharField(label='Page-title', max_length=100)
    # page_content = forms.CharField(label='Page-content', max_length=10000)

    class Meta: #Meta class allows us to specify details about the form, like what fields we want to show to the visitor, or what model we want to use to generate the HTML form 
        model = Page
        fields = '__all__' #makes it all fields is required