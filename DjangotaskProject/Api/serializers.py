from rest_framework import serializers
from .models import *


class usertypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_type']


class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'