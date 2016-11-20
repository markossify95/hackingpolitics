from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email')


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    topics = TopicSerializer(many=True)

    class Meta:
        model = Profile
        fields = ('user', 'type', 'id', 'about', 'topics', 'municipality')


class ProblemSerializer(serializers.ModelSerializer):
    topic = TopicSerializer()
    user = UserSerializer()

    class Meta:
        model = Problem
        fields = '__all__'


class SimpleProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = '__all__'


class UserTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTopic
        fields = '__all__'


class UserProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProblem
        fields = '__all__'
