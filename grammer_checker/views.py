from rest_framework.views import APIView
from grammer_checker.models import Grammer
from grammer_checker.serializers import *
from django.contrib.auth.models import User
from rest_framework.response import Response
from services.response import get_response


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
                return Response({ 'message':'user already exists' })
            else:
                User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                return Response({ 'message':'registration successfull' })
            
        else:
            return Response({ 'message':'invalid inputs' })
        
class DashboardAPI(APIView):
    def get(self, request):
        data=Grammer.objects.filter(user=request.user)
        serial=DashboardSerializer(data, many=True)
        return Response(serial.data)
    
    def post(self, request):
        serial=InputSerializer(data=request.data)
        if serial.is_valid():
            input=serial.validated_data['input']
            final_output=get_response(input)
            output_serial=ResponseSerializer(data=final_output)
            if output_serial.is_valid():
                corrected_text=output_serial.validated_data['corrected_text']
                mistakes=output_serial.validated_data['mistakes']
                explanation=output_serial.validated_data['explanation']

                Grammer.objects.create(input=input, corrected_text=corrected_text, mistakes=mistakes, explanation=explanation)
                return Response({ 'corrected_text':corrected_text, 'mistakes':mistakes, 'explanation':explanation })
            else:
                return Response({ 'invalid response recieved':'invalid response recieved from the server' })
        else:
            return Response({ 'message':'invalid input' })
                

            
