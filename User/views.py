from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, JSONParser

from.models import User
from Post.models import Xodim
from .serializers import *


class SignUp(APIView):
    parser_classes = (MultiPartParser, JSONParser)
    permission_classes = (permissions.AllowAny)
    def get(self, request):
        user = User.objects.all()
        ser = UserSer(user, many=True)
        return Response(ser.data)

    def post(self, request):
        ser = UserSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)


class XodimList(APIView):
    parser_classes = (MultiPartParser, JSONParser)
    def get(self, request):
        xodim = Xodim.objects.all()
        ser = XodimSer(xodim, many=True)
        return Response(ser.data)
    
    def post(self, request):
        ser = XodimSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)


class XodimDetail(APIView):
    parser_classes = (MultiPartParser, JSONParser)
    def get(self, request, id):
        xodim = Xodim.objects.get(id=id)
        ser = XodimSer(xodim)
        return Response(ser.data)
    
    def patch(self, request, id):
        xodim = Xodim.objects.get(id=id)
        ser = XodimSer(xodim, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)
    
    def delete(self, request, id):
        xodim = Xodim.objects.get(id=id)
        xodim.delete()
        return Response(status=204)