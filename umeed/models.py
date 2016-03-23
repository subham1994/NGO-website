from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class UmeedUsers(models.Model):
        user = models.OneToOneField(User)
        name = models.CharField(max_length=100)
        umeedId = models.CharField(max_length=10, blank=True)
        coremember = models.BooleanField(default=False)
        isAdmin = models.BooleanField(default=False)

        def __unicode__(self):
                return self.name


class UmeedNews(models.Model):
        title = models.CharField(max_length=200)
        body = models.TextField()
        pub_date = models.DateTimeField('date published')
        umeeduser = models.ForeignKey(UmeedUsers)

        def __unicode__(self):
                return self.title


class UsersPayment(models.Model):
        umeeduser = models.ForeignKey(UmeedUsers)
        paymentId = models.CharField(max_length=20, primary_key=True)
        amount = models.IntegerField()
        paydate = models.DateTimeField('date paid')
        hasdue = models.BooleanField(default=False)

        def __unicode__(self):
                return self.paymentId
