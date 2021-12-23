from django.conf.urls import url
from django.urls import path
from .views import *

urlpatterns = [
    path('user/<int:user_document>',userList.as_view(),name ='user_list'),
    path('user/<str:user_document>',userList.as_view(),name ='user_list'),
    path('login/',getToken.as_view(),name ='user_list'),
]