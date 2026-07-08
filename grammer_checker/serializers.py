from rest_framework.serializers import ModelSerializer
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
        fields=['user', 'input', 'time']

class InputSerializer(ModelSerializer):
    class Meta:
        model=Grammer
        fields=['input']
    
class ResponseSerializer(ModelSerializer):
    class Meta:
        model=Grammer
        fields=['corrected_text', 'mistakes', 'explanation']

class RegisterSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username', 'email', 'password']
