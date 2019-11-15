from django import forms
from wiki.models import Page


class PageForm(forms.ModelForm):
    """ Render and process a form based on the Page model. """
    model = Page

class CreatePageForm(forms.ModelForm):
    # page_title = forms.CharField(label='Page-title', max_length=100)
    # page_content = forms.CharField(label='Page-content', max_length=10000)

    class Meta:
        model = Page
        fields = '__all__'