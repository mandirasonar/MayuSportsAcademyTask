# views.py
from rest_framework import viewsets
from .models import Player
from .serializers import PlayerSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from .models import Coach
from .serializers import CoachSerializer
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')

    # Authenticate the user
    user = authenticate(username=username, password=password)
    
    if user is not None:
        
        token, created = Token.objects.get_or_create(user=user)
        
        
        return Response({"token": token.key}, status=status.HTTP_200_OK)
    else:
        
        return Response({"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)

class CoachLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            coach = Coach.objects.get(user=user)
            serializer = CoachSerializer(coach)
            return Response({'token': token.key, **serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

class CoachLogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'message': 'Successfully logged out'}, status=status.HTTP_200_OK)

class YourPlayerView(viewsets.ModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    http_method_names = ['get', 'post', 'put', 'delete']