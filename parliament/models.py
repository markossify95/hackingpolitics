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
    speech_type = models.CharField(max_length=30)
    speech = models.TextField()


class Act(models.Model):
    topic = models.ManyToManyField(Topic, through='Date')
    name = models.TextField()
    act_type = models.CharField(max_length=20)
    status = models.IntegerField(blank=True)  # 0-usvojen; 1-u proceduri; 2-odbijen;
    vote_yes = models.IntegerField(blank=True)
    vote_no = models.IntegerField(blank=True)


class Vote(models.Model):
    member = models.ForeignKey(Member)
    act = models.ForeignKey(Act)


class Date(models.Model):
    topic = models.ForeignKey(Topic)
    act = models.ForeignKey(Act)
    date = models.DateField()


class MemberAct(models.Model):
    member = models.ForeignKey(Member)
    act = models.ForeignKey(Act)
