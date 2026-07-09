from django.shortcuts import render
from student.models import Student
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, APIView
from api.serializers import studentSerializer
from employee.models import Employee
from .serializers import employeeSerializer
from django.http import Http404
from rest_framework import mixins,generics


# Create your views here.
@api_view(['GET','POST'])
def studentView(request):
    if request.method == 'GET':
        students=Student.objects.all()
        serializer = studentSerializer(students, many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    elif request.method =='POST':
        serialize = studentSerializer(data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response (serialize.data ,status=status.HTTP_201_CREATED)
        print(serialize.errors)
        return Response(serialize.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def studentDetailsView(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    # this is for geting sigle data
    if request.method== 'GET':
        serializer = studentSerializer(student)
        return Response (serializer.data,status=status.HTTP_200_OK)

    # this is for updating data
    elif request.method == 'PUT':
        serializer =studentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        #this is for deleting one data
    elif request.method== 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  



