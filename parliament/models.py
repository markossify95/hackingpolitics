from django.db import models
from django.contrib.auth.models import User
from citizen.models import Topic


class Member(models.Model):
    name = models.CharField(max_length=50)
    party = models.CharField(max_length=200)
    city = models.CharField(max_length=30)
    profession = models.CharField(max_length=50)


class Speech(models.Model):
    member = models.ForeignKey(Member)
    type = models.CharField(max_length=30)
    speech = models.TextField()


class Acts(models.Model):
    topics = models.ManyToManyField(Topic, through='Dates')
    name = models.CharField(max_length=50)
    status = models.IntegerField()  # 0-usvojen; 1-u proceduri; 2-odbijen;
    vote_yes = models.IntegerField()
    vote_no = models.IntegerField()


class Voting(models.Model):
    member = models.ForeignKey(Member)
    act = models.ForeignKey(Acts)


class Dates(models.Model):
    topics = models.ForeignKey(Topic)
    acts = models.ForeignKey(Acts)
    date = models.DateField()

