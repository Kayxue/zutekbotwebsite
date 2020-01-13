from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
# Create your views here.
class Userinfo(LoginRequiredMixin,TemplateView):
    template_name="userinfo.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = '使用者資訊'
        return context