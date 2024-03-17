from rest_framework.serializers import ModelSerializer
from yaml import serialize, serialize_all
from base.models import Category
from base.models import Provider
from django.contrib.auth.models import User
from rest_framework import serializers




class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProviderSerializer(serializers.ModelSerializer):
    profile_photo = serializers.ImageField(max_length=None, use_url=True)  # Use `use_url=True` to include the photo URL

    class Meta:
        model = Provider
        fields = '__all__'
    class Meta:
        model = Provider
        fields = '__all__'
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']

