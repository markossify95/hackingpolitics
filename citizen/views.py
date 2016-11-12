import bcrypt as bcrypt
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
from django.contrib.auth.forms import UserCreationForm


class UserInstance(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        # profile = Profile.objects.get(user_id=pk)
        user_serializer = UserSerializer(user)
        # profile_serializer = ProfileSerializer(profile)
        return Response(user_serializer.data)


class RegisterView(APIView):
    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        password = body['password']
        username = body['username']
        email = body['email']
        first_name = body['first_name']
        last_name = body['last_name']
        type = body['type']
        about = body['about']
        user = User(username=username, first_name=first_name,
                    last_name=last_name, email=email)
        user.set_password(password)
        user.save()
        profile = Profile(user_id=user.id, type=type, about=about)
        profile.save()
        final_user = authenticate(
            username=username, password=password)
        if final_user:
            login(request, final_user)
            kurac = UserSerializer(final_user)
            return Response(kurac.data)
        else:
            return HttpResponse(500)


class LoginView(APIView):
    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        print(body)
        password = body['password']
        username = body['username']
        user = User.objects.get(username=username)
        if user:
            authenticate(username=username,password=password)
            if user.is_authenticated():
                login(request, user)
                ds = UserSerializer(user)
                return Response(ds.data)
            else:
                return HttpResponseForbidden()


class ProfileInstance(APIView):
    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class ProblemInstance(APIView):
    def get_object(self, pk):
        try:
            return Problem.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = ProblemSerializer(user)
        return Response(serializer.data)


class ProblemInstancePost(APIView):
    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        title = body['title']
        description = body['description']
        date = body['date']
        topic = body['topic']
        topic_object = Topic.objects.get(pk=topic)
        user = body['user']
        user_object = User.objects.get(pk=user)
        problem = Problem(title=title,description=description,date=date,topic=topic_object,user=user_object)
        problem.save()
        serializer = ProblemSerializer(problem)
        return Response(serializer.data)


class ProblemFilter(APIView):
    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        date = body['date']
        res = Problem.objects.filter(topic_id__in=body['topic']).filter(date=date)
        serializer = ProblemSerializer(res,many=True)
        return Response(serializer.data)