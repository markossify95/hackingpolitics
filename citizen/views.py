from rest_framework.views import *
from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView,
                                     UpdateAPIView,
                                     DestroyAPIView
                                     )
from .models import *
from .JSONSerializer import *
from rest_framework.response import Response


# Create your views here.
class UserInstance(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
