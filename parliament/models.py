from django.db import models
from django.contrib.auth.models import User
from citizen.models import Topic


class Member(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    party = models.CharField(max_length=200)
    board_type = models.IntegerField(default=-1)
    bio = models.TextField(max_length=36000)


class Act(models.Model):
    topic = models.ManyToManyField(Topic, through='Date')
    name = models.TextField()
    act_type = models.CharField(max_length=20)
    status = models.IntegerField(blank=True)  # 1-usvojen; 0-u proceduri;
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
    vote = models.NullBooleanField()
