from rest_framework import serializers
from .models import *


class ActSerializer(serializers.ModelSerializer):
    class Meta:
        model = Act
        fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class VoteSerializer(serializers.ModelSerializer):
    acts = ActSerializer(many=True)
    member = MemberSerializer()

    class Meta:
        model = Vote
        fields = '__all__'


class BoardSerializer(serializers.ModelSerializer):
    member = MemberSerializer(many=True)

    class Meta:
        model = Board
        fields = ('name', 'member')


class MemberBoardSerializer(serializers.ModelSerializer):
    member = MemberSerializer()
    board = BoardSerializer()

    class Meta:
        model = MemberBoard
        fields = ('name', 'member', 'board')


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
