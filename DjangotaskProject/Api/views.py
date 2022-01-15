from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated








class product_api(APIView):
    permission_classes = [IsAuthenticated]
    #get all products
    def get(self, request, *args, **kwargs):
        product = Product.objects.order_by('price')
        serializer = productSerializer(instance=product, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    #post a product
    def post(self, request, *args, **kwargs):
        # request.data['user_id']=request.user.id
        serializers = productSerializer(data=request.data)
        # print(serializers)
        if serializers.is_valid():
            print("serializers")
            serializers.save()
            return Response({'message': serializers.data})
        return Response({'message': serializers.errors})


class userproducts(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk, format=None):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response("Sorry! Doesn't Exist🙁")
        products = Product.objects.filter(user=user)

        serializer = productSerializer(products, many=True)
        return Response(serializer.data)
