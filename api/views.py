from django.shortcuts import render
from student.models import Student
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, APIView
from api.serializers import studentSerializer
from employee.models import Employee
from .serializers import employeeSerializer
from django.http import Http404
from rest_framework import mixins,generics, viewsets


"""
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

"""

# this is for students mixins used in classbased view
class studentView(mixins.ListModelMixin,mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = studentSerializer

    def get(self, request):
        return self.list(request)
    
    def post(self, request):
        return self.create(request)
    
class studentDetailsView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = studentSerializer

    def get(self, request,pk):
        return self.retrieve(request,pk)

    def put(self, request,pk):
        return self.update(request,pk)
    
    def delete(self, request, pk):
        return self.delete(request,pk)
            



"""
# class based views
class Employees(APIView):
    def get(self, request):
        employee = Employee.objects.all()
        serializer = employeeSerializer(employee, many=True)
        return Response (serializer.data,status=status.HTTP_200_OK)
    
    def post(self , request):
        serializer = employeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class EmployeesDetails(APIView):
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404
        
    def get(self,request,pk):
        employee = self.get_object(pk)
        serializer = employeeSerializer(employee)
        return Response(serializer.data , status=status.HTTP_200_OK)
    
    def put(self,request, pk):
        employee = self.get_object(pk)
        serializer = employeeSerializer(employee, data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
"""

"""
# mixins start here
class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView): 
    queryset = Employee.objects.all()
    serializer_class = employeeSerializer

    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)
    


class EmployeesDetails(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Employee.objects.all()
    serializer_class = employeeSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk)   

    def put(self , request , pk):
        return self.update(request, pk) 
    
    def delete(self, request,pk):
        return self.destroy(request,pk)
    
"""

# Generics start for here
"""
class Employees(generics.ListCreateAPIView ):     # in this they do both listing and creating api view 
    queryset = Employee.objects.all()
    serializer_class = employeeSerializer


class EmployeesDetails(generics.RetrieveUpdateDestroyAPIView):    # this thye do three work retriving sigle , updating and destroy
    queryset = Employee.objects.all()
    serializer_class = employeeSerializer
    lookup_field = 'pk'

    
"""


#Viewsets

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = employeeSerializer