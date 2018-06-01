from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible

from django.db import models
from django.core.urlresolvers import reverse

from photo.fields import ThumbnailImageField

from django.contrib.auth.models import User

# Create your models here.

@python_2_unicode_compatible
class Album(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField('One Line Description', max_length=100, blank=True)
    #owner = models.ForeignKey(User, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('photo:album_detail', args=(self.id,))

@python_2_unicode_compatible
class Photo(models.Model):
    album = models.ForeignKey(Album , default=0)
    title = models.CharField(max_length=50 , default=0)
    image = ThumbnailImageField(upload_to='photo/%Y/%m' , default=0)
    description = models.TextField('Photo Description', blank=True , default=0)
    upload_date = models.DateTimeField('Upload Date', auto_now_add=True)
    owner = models.ForeignKey(User, null=True, default=0)
    cnt = models.CharField(max_length=50, default=0)
    price = models.CharField(max_length=50, default=0)
    Subscription_ratings=models.CharField(max_length=50 , default=0)
    purchase_after_sub=models.CharField(max_length=50, default=0)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('photo:photo_detail', args=(self.id,))
