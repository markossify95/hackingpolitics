from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
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



