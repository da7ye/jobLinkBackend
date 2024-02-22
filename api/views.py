from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from base.models import Category
from base.models import Provider
from .serializers import CategorySerializer
from .serializers import ProviderSerializer
from .serializers import UserSerializer
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/categories',
        'GET /api/categoryProviders/:id',
        'GET /api/providers',
        'GET /api/providers/:id',
        'GET /api/users',
        'GET /api/users:id',
    ]
    return Response(routes,)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def getCategories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def getCategorieProvider(request, pk):
    categoryProviders = Category.objects.get(id=pk)
    serializer = CategorySerializer(categoryProviders)
    return Response(serializer.data) 


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def getProviders(request):
    providers = Provider.objects.all()
    serializer = ProviderSerializer(providers, many=True)
    return Response(serializer.data) 


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def getProvider(request, pk):
    provider = Provider.objects.get(id=pk)
    serializer = ProviderSerializer(provider)
    return Response(serializer.data) 


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def getUsers(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data) 


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def getUser(request, pk):
    user = User.objects.get(id=pk)
    serializer = UserSerializer(user)
    return Response(serializer.data) 

@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer =  UserSerializer(instance=user)
    return Response({"token": token.key, "user": serializer.data})

@api_view(['POST'])
def signUp(request):
    serializer =  UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token" : token.key, "user" : serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def testToken(request):
    return Response({"passed for {}".format(request.user.username)})