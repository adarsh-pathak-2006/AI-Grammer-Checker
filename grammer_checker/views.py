from rest_framework.views import APIView
from grammer_checker.models import Grammer
from grammer_checker.serializers import *
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from services.response import get_response
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated


class RegisterAPI(APIView):
    def post(self, request):
        serial=RegisterSerializer(data=request.data)
        if serial.is_valid():
            first_name=serial.validated_data['first_name']
            last_name=serial.validated_data['last_name']
            username=serial.validated_data['username']
            email=serial.validated_data['email']
            password=serial.validated_data['password']

            if User.objects.filter(username=username).exists():
                return Response({ 'message':'user already exists' }, status=status.HTTP_409_CONFLICT)
            else:
                User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                return Response({ 'message':'registration successfull' }, status=status.HTTP_201_CREATED)
            
        else:
            return Response({ 'message':'invalid inputs', 'errors': serial.errors }, status=status.HTTP_400_BAD_REQUEST)
        
class DashboardAPI(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request):
        data=Grammer.objects.filter(user=request.user)
        serial=DashboardSerializer(data, many=True)
        return Response(serial.data)
    
    def post(self, request):
        serial=InputSerializer(data=request.data)
        if serial.is_valid():
            user_input=serial.validated_data['input']
            try:
                final_output=get_response(user_input)
            except Exception as e:
                return Response({ 'message':'AI service error', 'error': str(e) }, status=status.HTTP_502_BAD_GATEWAY)

            output_serial=ResponseSerializer(data=final_output)
            if output_serial.is_valid():
                corrected_text=output_serial.validated_data['corrected_text']
                mistakes=output_serial.validated_data['mistakes']
                explanation=output_serial.validated_data['explanation']

                Grammer.objects.create(input=user_input, corrected_text=corrected_text, mistakes=mistakes, explanation=explanation, user=self.request.user)
                return Response({ 'corrected_text':corrected_text, 'mistakes':mistakes, 'explanation':explanation })
            else:
                return Response({ 'message':'invalid response from AI', 'errors': output_serial.errors }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({ 'message':'invalid input', 'errors': serial.errors }, status=status.HTTP_400_BAD_REQUEST)
                
class IndividualAPI(RetrieveAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=IndividualSerializer

    def get_queryset(self):
        return Grammer.objects.filter(user=self.request.user)
