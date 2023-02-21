from django.shortcuts import render
from .models import Food
from .serializers import FoodSerializers

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.
@api_view(['GET', 'POST'])
def food_list(request):
    if request.method == "GET":
        foods = Food.objects.all()
        serializer = FoodSerializers(foods, many=True)
        return Response(serializer.data)
    
    if request.method == "POST":
        serializer = FoodSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        

@api_view(["GET", "PUT", "DELETE"])
def food_detail(request, id):
    try:
        food = Food.objects.get(pk=id)
    except Food.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = FoodSerializers(food)
        return Response(serializer.data)
    
    if request.method == "PUT":
        serializer = FoodSerializers(food,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


