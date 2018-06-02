from django.conf.urls import url

from account.views import *

urlpatterns = [

    url(r'^account/$',mypage.as_view(),name='mypage'),

    ]