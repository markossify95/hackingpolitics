from django.db import models
from django.contrib.auth.models import User
from citizen.models import Topic


class Member(models.Model):
    name = models.CharField(max_length=50)
    party = models.CharField(max_length=200)
    bio = models.TextField(max_length=36000)
    image = models.TextField(default='')

class Board(models.Model):
    name = models.CharField(max_length=200)
    member = models.ManyToManyField(Member)


class MemberBoard(models.Model):
    member = models.ForeignKey(Member)
    board = models.ForeignKey(Board)


class Act(models.Model):
    topic = models.ManyToManyField(Topic, through='Date')
    name = models.TextField(max_length=1000)
    status = models.IntegerField(blank=True)  # 1-usvojen; 0-u proceduri;
    vote_yes = models.IntegerField(blank=True, default=0)
    vote_no = models.IntegerField(blank=True, default=0)


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
