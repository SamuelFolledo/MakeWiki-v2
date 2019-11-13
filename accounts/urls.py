from django.urls import path
from accounts.views import SignUpView


urlpatterns = [
    path('signup', SignUpView.as_view(), name='signup'),
    # path('<str:slug>/', PageDetailView.as_view(), name='wiki-details-page'),
]