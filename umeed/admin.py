from django.contrib import admin
from umeed.models import UmeedUsers
from umeed.models import UmeedNews
from umeed.models import UsersPayment

# Register your models here.
admin.site.register(UmeedUsers)
admin.site.register(UmeedNews)
admin.site.register(UsersPayment)