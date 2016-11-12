from rest_framework import serializers
from .models import *


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class SpeechSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speech
        fields = '__all__'


class ActsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Acts
        fields = '__all__'


class VotingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voting
        fields = '__all__'


class DatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dates
        fields = '__all__'

