from django.shortcuts import render
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.contrib.auth import login

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.serializers import AuthTokenSerializer

from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView


from .models import User
from .serializers import UserSerializer
# Create your views here.


class UsersAPI(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        """Posts to the database, creates a new user"""
        user_serializer = self.get_serializer(data=request.data)

        if user_serializer.is_valid():
            user = user_serializer.save()
            return Response({
                "message": "New User created successfully",
                "user": UserSerializer(user, context=self.get_serializer_context()).data,
                "token": AuthToken.objects.create(user)[1]}, status.HTTP_201_CREATED)

        return Response(user_serializer.errors, status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        """Get all users"""
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)
        return Response({"all_users": users_serializer.data}, status.HTTP_200_OK)


class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        auth_serializer = AuthTokenSerializer(data=request.data)
        print (auth_serializer)
        if auth_serializer.is_valid():
            user = auth_serializer.validated_data['user']
            login(request, user)
            return super(LoginAPI, self).post(request, format=None)
        
        return Response(auth_serializer.errors, status.HTTP_400_BAD_REQUEST)


class SingleUserAPI(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        """Gets a specific user"""
        user_serializer = self.get_serializer(request.user)
        return Response(user_serializer.data, status.HTTP_200_OK)


# @api_view(["GET", "POST", "PUT", "DELETE"])
# def all_users(request):
#     if request.method == "GET":
#         users = User.objects.all()
#         users_serializer = UserSerializer(users, many=True)
#         return Response(users_serializer.data, status.HTTP_200_OK)
    
#     elif request.method == "POST":
#         user_data = JSONParser().parse(request)
#         user_serializer = UserSerializer(data=user_data)

#         if user_serializer.is_valid():
#             user_serializer.save()
#             return Response({ "message": "New User created successfully", "user": user_serializer.data }, status.HTTP_201_CREATED)

#         return Response(user_serializer.errors, status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == "PUT":
#         user_data = JSONParser().parse(request)
#         user = User.objects.get(id=user_data['id'])
#         user_serializer = UserSerializer(user, data=user_data)

#         if user_serializer.is_valid():
#             user_serializer.save()
#             return Response({"message": f"User {user_data['email']} updated successfully", "user": user_serializer.data }, status.HTTP_200_OK)
        
#         return Response(user_serializer.errors, status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == "DELETE":
#         user = User.objects.get(id=id)
#         user.delete()
#         return Response("User deleted successfully")


# @api_view
# def upload_file(request):
#     file = request.FILES['file']
#     filename = default_storage.save(file.name, file)
#     return Response(filename, status.HTTP_201_CREATED)

# class UserViewSet(viewsets.ModelViewSet):

#     queryset = User.objects.all()
#     serializer_class = UserSerializer