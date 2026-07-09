from rest_framework.serializers import ModelSerializer, Serializer, CharField, JSONField
from django.contrib.auth.models import User
from grammer_checker.models import Grammer


class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['id', 'first_name', 'last_name', 'username', 'email']

class IndividualSerializer(ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=Grammer
        fields='__all__'

class DashboardSerializer(ModelSerializer):
    class Meta:
        model=Grammer
        fields=['id', 'user', 'input', 'time']

class InputSerializer(ModelSerializer):
    class Meta:
        model=Grammer
        fields=['input']

class ResponseSerializer(Serializer):
    corrected_text=CharField()
    mistakes=JSONField()
    explanation=JSONField()

class RegisterSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username', 'email', 'password']
        extra_kwargs={
            'password': {'write_only': True},
        }
