from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    users = models.ManyToManyField(User, through='Problem')
    category = models.CharField(max_length=50, default='Uncategorized', null=False)
    board = models.ForeignKey("parliament.Board")


class Profile(models.Model):
    def as_dict(self):
        return {
            "id": self.id,
            "user": self.user,
            "type": self.type,
            "about": self.about,
            "topics": self.topics,
            "municip": self.municipality
        }

    user = models.OneToOneField(User, related_name='user', on_delete=models.CASCADE)
    type = models.CharField(default="0", max_length=6)  # 0 - civil, 1 - organization, 2 - journalist, 3 - pravno lice
    about = models.TextField(blank=True)
    topics = models.ManyToManyField(Topic, through='UserTopic')
    municipality = models.CharField(default='N/A', max_length=50)
    image = models.TextField(default='')

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)


class UserTopic(models.Model):
    topic = models.ForeignKey(Topic)
    user = models.ForeignKey(Profile)


class Problem(models.Model):
    topic = models.ForeignKey(Topic)
    user = models.ForeignKey(User)
    date = models.DateField(null=False)
    status = models.IntegerField(default=0)  # 0 - postavljen, 1 - u procesu 2 - resen
    title = models.TextField(max_length=140)
    description = models.TextField(default="")
    votes_up = models.IntegerField(default=0)
    votes_down = models.IntegerField(default=0)
    image = models.TextField(default='')


class UserProblem(models.Model):
    user = models.ForeignKey(Profile)
    problem = models.ForeignKey(Problem)
    vote_type = models.IntegerField(null=False, default=0)  # 0 - no! ; 1 - yes!


class ProblemSolved(models.Model):
    problem = models.ForeignKey(Problem)
    member = models.ForeignKey('parliament.Member')
    description = models.TextField(max_length=10000)
