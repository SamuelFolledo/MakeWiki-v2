from django.urls import path
from wiki.views import PageListView, PageDetailView, PageCreateView

app_name = "wiki"

urlpatterns = [
    path('', PageListView.as_view(), name='wiki-list-page'),
    path('<str:slug>/', PageDetailView.as_view(), name='wiki-details-page'),
    path('wiki/create/', PageCreateView.as_view(), name='wiki-create-page'),
    path('thanks/', PageDetailView.as_view(), name='wiki-thanks-page'),
]
