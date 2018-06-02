from django.contrib import admin
from account.models import *

# Register your models here.

class AccountAdmin(admin.ModelAdmin):
    list_display = ('account', 'address','group','owner')



admin.site.register(Account, AccountAdmin)

