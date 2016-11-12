from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    users = models.ManyToManyField(User, through='Problem')
    category = models.CharField(max_length=50, default='Uncategorized', null=False)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    type = models.IntegerField(null=False)  # 0 - civil, 1 - organization, 2 - journalist, 3 - pravno lice
    about = models.TextField(blank=True)
    topics = models.ManyToManyField(Topic, through='UserTopic')
    municipality = models.CharField(default='N/A', max_length=50)


class UserTopic(models.Model):
    topic = models.ForeignKey(Topic)
    user = models.ForeignKey(Profile)


class Problem(models.Model):
    topic = models.ForeignKey(Topic)
    user = models.ForeignKey(User)
    date = models.DateField(null=False)
    title = models.TextField(max_length=140)
    description = models.TextField(default="")


class UserProblem(models.Model):
    user = models.ForeignKey(Profile)
    problem = models.ForeignKey(Problem)
    vote_type = models.IntegerField(null=False, default=0)  # 0 - no! ; 1 - yes!
