from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.parsers import MultiPartParser, JSONParser

from .models import User
from Post.models import Ish_Turi, Xodim
from .serializers import UserSer, XodimSer


class SignUp(ListCreateAPIView):
    parser_classes = [MultiPartParser, JSONParser]
    queryset = User.objects.all()
    serializer_class = UserSer


class XodimList(ListCreateAPIView):
    parser_classes = [MultiPartParser, JSONParser]
    queryset = Xodim.objects.all()
    serializer_class = XodimSer


class XodimDetail(RetrieveUpdateDestroyAPIView):
    parser_classes = [MultiPartParser, JSONParser]
    queryset = Xodim.objects.all()
    serializer_class = XodimSer


# class SignUp(APIView):
#     parser_classes = [MultiPartParser, JSONParser]
#     permission_classes = [permissions.AllowAny]
#     def get(self, request):
#         user = User.objects.all()
#         ser = UserSer(user, many=True)
#         return Response(ser.data)

    # def post(self, request):
    #     ser = UserSer(data=request.data)
    #     if ser.is_valid():
    #         ser.save()
    #         return Response(ser.data)
    #     return Response(ser.errors)


# class XodimList(APIView):
#     parser_classes = [MultiPartParser, JSONParser]
#     def get(self, request):
#         xodim = Xodim.objects.all()
#         ser = XodimSer(xodim, many=True)
#         return Response(ser.data)
    
#     def post(self, request):
#         ish_list = request.data.getlist('ish_turi', [])
#         ser = XodimSer(data=request.data)
#         if ser.is_valid():
#             ser.save()
#             # news = ser.save()
#             # for x in ish_list:
#             #     p = Ish_Turi.objects.create(name=x)
#             #     news.ish_turi.add(p)
#             return Response(ser.data)
#         return Response(ser.errors)


# class XodimDetail(APIView):
#     parser_classes = [MultiPartParser, JSONParser]
#     def get(self, request, id):
#         xodim = Xodim.objects.get(id=id)
#         ser = XodimSer(xodim)
#         return Response(ser.data)
    
#     def patch(self, request, id):
#         xodim = Xodim.objects.get(id=id)
#         ser = XodimSer(xodim, data=request.data, partial=True)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data)
#         return Response(ser.errors)
    
#     def delete(self, request, id):
#         xodim = Xodim.objects.get(id=id)
#         xodim.delete()
#         return Response(status=204)