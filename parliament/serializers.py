from rest_framework import serializers
from .models import *


class ActSerializer(serializers.ModelSerializer):
    class Meta:
        model = Act
        fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):
    acts = ActSerializer()

    class Meta:
        model = Member
        fields = ('member', 'acts')


class VoteSerializer(serializers.ModelSerializer):
    act = ActSerializer()

    class Meta:
        model = Vote
        fields = '__all__'


# NO NEED ???
class DateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Date
        fields = '__all__'


class MemberActSerializer(serializers.ModelSerializer):
    # member = MemberSerializer()
    # act = ActSerializer()
    # date = DateSerializer()

    class Meta:
        model = MemberAct
        # fields = ('member', 'act', 'date')
