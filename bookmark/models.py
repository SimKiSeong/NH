from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.contrib.auth.models import User
from photo.models import *
# Create your models here.

@python_2_unicode_compatible
class Bookmark(models.Model):
    title = models.ForeignKey(Album, blank=True,null=True)
    amount = models.CharField(max_length=100, blank=True, null=True)
    price = models.CharField(max_length=100, blank=True, null=True)
    owner = models.ForeignKey(User, null=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return str(self.title)

# 그룹을 만들건데 이 그룹이 사용자로 되는거지
class SubGroup(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    price = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return str(self.title)


# 구독한 목록 객채
class SubList(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    price = models.CharField(max_length=100, blank=True, null=True)
    owner = models.ForeignKey(SubGroup, null=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return str(self.title)

