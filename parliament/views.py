from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers as srl
from .models import *
from .serializers import *
from django.http import HttpResponse, HttpResponseForbidden
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
import bs4 as bs
import urllib.request


class ActView(APIView):
    def get_object(self, pk):
        try:
            return Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        member = self.get_object(pk)
        serializer = MemberSerializer(member)
        return Response(serializer.data)


class MemberInstance(APIView):
    def get_object(self, pk):
        try:
            return Member.objects.get(pk=pk)
        except Member.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        member = self.get_object(pk)
        serializer = MemberSerializer(member)
        return Response(serializer.data)


class MemberActsView(APIView):
    def get(self, request, fk):
        query_set = MemberAct.objects.filter(member=fk)
        serializer = MemberActSerializer(data=query_set)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            raise Http404()


class VotesView(APIView):
    def get_object(self, fk):
        try:
            return Vote.objects.get(member=fk)
        except Vote.DoesNotExist:
            raise Http404()

    def get(self, request, fk):
        query_set = self.get_object(fk)
        serializer = VoteSerializer(data=query_set)
        if serializer.is_valid():
            return Response(serializer.data)
        else:
            raise Http404()


class Recommendation(APIView):
    def get(self, request, id):
        result_set = Member.objects.raw(
            "SELECT * FROM parliament_member WHERE id in (SELECT member_id from parliament_board_member WHERE board_id = " + id + ") ")

        data = srl.serialize('json', result_set, fields=('id', 'name', 'party', 'image', 'bio'))
        return HttpResponse(data)
