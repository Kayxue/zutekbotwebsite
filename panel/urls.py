from django.urls import path
from .views import Userinfo,Panel

urlpatterns = [
    path('',Panel.as_view()),
    path('userinfo/',Userinfo.as_view()),
]