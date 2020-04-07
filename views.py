
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .SQLAlchemy import create_user
from rest_framework.response import Response

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
            user_python = User(first_name=first_name, last_name=last_name, birth_date=birth_date, gender=gender, user_name=user_name, password=password )
            create_user(user_python)
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)












