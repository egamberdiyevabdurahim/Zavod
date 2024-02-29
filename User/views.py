from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, UpdateAPIView
from rest_framework.parsers import MultiPartParser, JSONParser
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from Post.models import Ish_Turi, Xodim
from .serializers import UserSer, XodimSer, ChangePasswordSerializer


class ChangePasswordView(APIView):
    parser_classes = [MultiPartParser, JSONParser]
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            user = self.request.user
            old_password = serializer.data.get('old_password')
            new_password = serializer.data.get('new_password')

            if not user.check_password(old_password):
                return Response({'detail': 'Old password is incorrect.'})

            user.set_password(new_password)
            user.save()
            refresh = RefreshToken.for_user(user)
            access = str(refresh.access_token)
            return Response({'detail': 'Password changed successfully.',
                             'access': access,
                             'refresh': str(refresh)
                             })

        return Response(serializer.errors)


class SignUp(ListCreateAPIView):
    parser_classes = [MultiPartParser, JSONParser]
    queryset = User.objects.all()
    serializer_class = UserSer

class Userdetail(APIView):
    permission_classes = [IsAuthenticated,]
    def get(self, request, id):
        user = User.objects.get(id=id)
        ser = UserSer(user)
        return Response(ser.data)
    
    def patch(self, request, id):
        user = User.objects.filter(id=id).first()
        ser = UserSer(data=request.data, instance=user, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

class XodimList(ListCreateAPIView):
    parser_classes = [MultiPartParser, JSONParser]
    queryset = Xodim.objects.all()
    serializer_class = XodimSer


# class XodimDetail(RetrieveUpdateDestroyAPIView):
#     parser_classes = [MultiPartParser, JSONParser]
#     queryset = Xodim.objects.all()
#     serializer_class = XodimSer


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


class XodimDetail(APIView):
    parser_classes = [MultiPartParser, JSONParser]
    def get(self, request, id):
        xodim = Xodim.objects.get(id=id)
        ser = XodimSer(xodim)
        return Response(ser.data)
    
    def patch(self, request, id):
        ish = request.data.getlist('ish_turi', [])
        xodim = Xodim.objects.get(id=id)
        ser = XodimSer(data=request.data, partial=True)
        if ser.is_valid():
            news = ser.save()
            if ish:
                news.ish_turi.clear()
                for x in ish:
                    news.ish_turi.add(x)
            return Response(ser.data)
        return Response(ser.errors)
    
    def delete(self, request, id):
        xodim = Xodim.objects.get(id=id)
        xodim.delete()
        return Response(status=204)