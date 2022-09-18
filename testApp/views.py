from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from testApp.serializer import StudentSerializerr
from .models import Student
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

'''@api_view(['GET','POST','PUT','PATCH'])
def home(request):
    response={'status':200,'message':"hi,from rest"}
    return Response(response)'''
@api_view(['POST'])
def login_api(request):
    try:
        data=request.data
        username=request.data('username')
        password=request.data("password")
        user=authenticate(username=username,password=password)
        if user:
            token ,_=Token.objects.get_or_create(user=user)
            return Response({"status":200,"token":str(token)})
        return Response({"status":300,"message":"Invalid credentials"})
    except Exception as e:
        print(e)
    return Response({"status":400,"message":"something went wrong"})

@api_view(['GET'])
def get_students(request):
    response = {'status':200}
    student_objs=Student.objects.all()
    serializer=StudentSerializerr(student_objs,many=True)
    response['data']=serializer.data
    return Response(response)

@api_view(['POST'])
def post_students(request):
    response = {'status':200}
    data=request.data
    serializer=StudentSerializerr(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(response)

    return Response(serializer.errors)

@api_view(['PATCH'])
def patch_students(request):
    response={"status":200}
    data=request.data
    try:
        obj=Students.objects.get(id=data.get('id'))
        serializer=StudentSerializerr(obj,data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            response['data']=serializer.data
            return Response(response)

        return Response(serializer.errors)
    except Exception as e:
        print(e)

    return Response({"status":400,"message":'invalid id'})
