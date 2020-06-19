from django.urls import *
from .views import *

urlpatterns = [
    path('',AllCommand.as_view())
]