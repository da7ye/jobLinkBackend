from rest_framework.serializers import ModelSerializer
from base.models import Category
from base.models import Provider
from django.contrib.auth.models import User


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ProviderSerializer(ModelSerializer):
    class Meta:
        model = Provider
        fields = '__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']

