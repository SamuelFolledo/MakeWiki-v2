from django.urls import path

# from api.views import QuestionList, QuestionDetail
from api.views import PageList, PageDetail

# urlpatterns = [
#     path('wiki/', QuestionList.as_view(), name='wiki_list'),
#     path('wiki/<int:pk>', QuestionDetail.as_view(), name='wiki_detail')
# ]

urlpatterns = [
    path('', PageList.as_view(), name='wiki-list-page'),
    path('<str:slug>/', PageDetail.as_view(), name='wiki-details-page'),
]