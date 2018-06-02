from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from account.models import Account

from django.views.generic.edit import FormView
from django.core.urlresolvers import reverse_lazy
from mysite.views import LoginRequiredMixin

class mypage(LoginRequiredMixin,ListView):
    model=Account
    def get_queryset(self):
        return Account.objects.filter(owner=self.request.user)