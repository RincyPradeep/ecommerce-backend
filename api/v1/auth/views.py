from rest_framework.response import Response
import requests
import json
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
 
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth.models import User


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['username'] = user.username

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(["POST"])
@permission_classes([AllowAny])
def create(request):
    
    first_name = request.data["first_name"]
    last_name = request.data["last_name"]
    email = request.data["email"]
    username = request.data["username"]
    password = request.data["password"]

    if not User.objects.filter(username=username).exists():
        user = User.objects.create_user(
            first_name = first_name,
            last_name = last_name,
            email = email,
            username = username,
            password = password
        )

        headers={
            "content-Type" : "application/json" 
        }
        data={
            "username" : username,
            "password" : password
        }

        # for login automatically after signup
        protocol = "http://"
        if request.is_secure():
            protocol = "https://"
        host = request.get_host()

        url = protocol + host +"/api/v1/auth/token/"
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response_data = {
            "status_code" : 6000,
            "data" : response.json(),
            "message" : "Account Created"
        }
    else:
        response_data = {
            "status_code" : 6001,
            "message" : "This account already exist."
        }    
    
    return Response(response_data)


        