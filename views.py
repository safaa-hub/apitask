from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .SQLAlchemy import create_user, is_valid, get_user
from rest_framework.response import Response
from .serializers import UserSerializer
from myproject.myapp.models import User


# Create your views here.


class RegisterView(APIView):
    @api_view(['POST'])
    def create_new(self, request):
        data = request.DATA
        if data is not None:

            first_name = request.DATA.get('first_name')
            last_name = request.DATA.get('last_name')
            birth_date = request.DATA.get('birth_date')
            gender = request.DATA.get('gender')
            user_name = request.DATA.get('user_name')
            password = request.DATA.get('password')
            user_python = User(first_name=first_name, last_name=last_name, birth_date=birth_date, gender=gender,
                               user_name=user_name, password=password)
            create_user(user_python)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)


class LoginView(APIView):
    @api_view(['POST'])
    def login(self, request):
        data = request.DATA
        if data is not None:
            user_name = request.DATA.get('user_name')
            password = request.DATA.get('password')
            if is_valid(user_name, password):
                return Response(status=status.HTTP_202_ACCEPTED)
            else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)


class GetUserView(APIView):
    @api_view(['POST'])
    def get(self, request):
        data = request.DATA
        if data is not None:
            id = request.DATA.get('id')
            user = get_user(id)
            serialized_user = UserSerializer(user)
            return Response(serialized_user, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)
