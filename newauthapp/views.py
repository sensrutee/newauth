from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login
from .serializers import CustomUserSerializer
import boto3



def save_to_dynamodb(data):
    aws_access_key_id = "YOUR_ACCESS_KEY"
    aws_secret_access_key = "YOUR_SECRET_KEY"
    aws_default_region = 'ap-south-1'

    # Initialize DynamoDB client with credentials and region
    dynamodb = boto3.resource('dynamodb', region_name=aws_default_region,
                              aws_access_key_id=aws_access_key_id,
                              aws_secret_access_key=aws_secret_access_key)

    table_name = 'YourTableName'  # Replace with your DynamoDB table name
    table = dynamodb.Table(table_name)

    # Save data to DynamoDB table
    response = table.put_item(Item=data)

    return response

class RegistrationView(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        print(request.data, "============")
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)

            response_data = {
                'refresh': str(refresh)
,
                'access': str(refresh.access_token),
            }
            return Response(response_data, status=201)
        return Response(serializer.errors, status=400)




class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)

            response_data = {
                'refresh': str(refresh)
,
                'access': str(refresh.access_token),
            }
            return Response(response_data, status=200)
        return Response({'error': 'Invalid credentials'}, status=401)