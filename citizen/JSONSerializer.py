from rest_framework.serializers import ModelSerializer
from .models import *


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = {
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
        }
