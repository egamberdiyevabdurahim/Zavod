from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.parsers import MultiPartParser, JSONParser

from .serializers import *
from .models import *


class PhotoEditView(APIView):
    def patch(self, request, id):
        photo = Photo.objects.get(id=id)
        rasm = request.data.get('photo')
        photo.photo = rasm
        photo.save()
        return Response({'message': 'successfully'})
    
    def delete(self, request, id):
        photo = Photo.objects.get(id=id)
        photo.delete()
        return Response({'message': 'deleted successfully'})


class PhotoList(ListCreateAPIView):
    parser_classes = (MultiPartParser, JSONParser)
    queryset = Photo.objects.all()
    serializer_class = PhotoSer


class IshTuriList(ListCreateAPIView):
    parser_classes = (MultiPartParser, JSONParser)
    queryset = Ish_Turi.objects.all()
    serializer_class = Ish_TuriSer


class Ish_TuriDetail(RetrieveUpdateDestroyAPIView):
    parser_classes = (MultiPartParser, JSONParser)
    queryset = Ish_Turi.objects.all()
    serializer_class = Ish_TuriSer


# class BulimList(RetrieveUpdateDestroyAPIView):
#     parser_classes = (MultiPartParser, JSONParser)
#     queryset = Bulim.objects.all()
#     serializer_class = BulimSer


# class BulimDetail(RetrieveUpdateDestroyAPIView):
#     parser_classes = (MultiPartParser, JSONParser)
#     queryset = Bulim.objects.all()
#     serializer_class = BulimSer


class MahsulotList(ListCreateAPIView):
    parser_classes = (MultiPartParser, JSONParser)
    queryset = Mahsulot.objects.all()
    serializer_class = MahsulotSer


class MahsulotDetail(RetrieveUpdateDestroyAPIView):
    parser_classes = (MultiPartParser, JSONParser)
    queryset = Mahsulot.objects.all()
    serializer_class = MahsulotSer


class XatolarList(ListCreateAPIView):
    parser_classes = (MultiPartParser, JSONParser)
    queryset = Xatolar.objects.all()
    serializer_class = XatolarSer


class XatolarDetail(RetrieveUpdateDestroyAPIView):
    parser_classes = (MultiPartParser, JSONParser)
    queryset = Xatolar.objects.all()
    serializer_class = XatolarSer


# class MissedList(ListCreateAPIView):
#     parser_classes = (MultiPartParser, JSONParser)
#     queryset = Missed.objects.all()
#     serializer_class = MissedSer


# class MissedDetail(RetrieveUpdateDestroyAPIView):
#     parser_classes = (MultiPartParser, JSONParser)
#     queryset = Missed.objects.all()
#     serializer_class = MissedSer


# class PhotoList(APIView):
#     parser_classes = (MultiPartParser, JSONParser)
#     def get(self, request):
#         photos = Photo.objects.all()
#         ser = PhotoSer(photos, many=True)
#         return Response(ser.data)
    
#     def post(self, request):
#         ser = PhotoSer(data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data, status=201)
#         return Response(ser.errors, status=400)


# class IshTuriList(APIView):
#     parser_classes = (MultiPartParser, JSONParser)
#     def get(self, request):
#         ishturi = Ish_Turi.objects.all()
#         ser = Ish_TuriSer(ishturi, many=True)
#         return Response(ser.data)
    
#     def post(self, request):
#         ser = Ish_TuriSer(data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data, status=201)
#         return Response(ser.errors, status=400)


# class Ish_TuriDetail(APIView):
#     parser_classes = (MultiPartParser, JSONParser)
#     def get(self, request, id):
#         ishturi = Ish_Turi.objects.get(id=id)
#         ser = Ish_TuriSer(ishturi)
#         return Response(ser.data)
    
#     def patch(self, request, id):
#         ishturi = Ish_Turi.objects.get(id=id)
#         ser = Ish_TuriSer(ishturi, data=request.data, partial=True)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data, status=201)
#         return Response(ser.errors, status=400)
    
#     def delete(self, request, id):
#         ishturi = Ish_Turi.objects.get(id=id)
#         ishturi.delete()
#         return Response(status=204)


class BulimList(APIView):
    parser_classes = (MultiPartParser, JSONParser)
    def get(self, request):
        """
        name : string
        bulim_id : string (unique)
        user : id
        """
        bulim = Bulim.objects.all()
        ser = BulimSer(bulim, many=True)
        return Response(ser.data)
    
    def post(self, request):
        """
        name : string
        bulim_id : string (unique)
        user : id
        """
        ser = BulimSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=201)
        return Response(ser.errors, status=400)


class BulimDetail(APIView):
    parser_classes = (MultiPartParser, JSONParser)
    def get(self, request, id):
        bulim = Bulim.objects.get(id=id)
        ser = BulimSer(bulim)
        return Response(ser.data)
    
    def patch(self, request, id):
        bulim = Bulim.objects.get(id=id)
        ser = BulimSer(bulim, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=201)
        return Response(ser.errors, status=400)
    
    def delete(self, request, id):
        bulim = Bulim.objects.get(id=id)
        bulim.delete()
        return Response(status=204)


# class MahsulotList(APIView):
#     parser_classes = (MultiPartParser, JSONParser)
#     def get(self, request):
#         mahsulot = Mahsulot.objects.all()
#         ser = MahsulotSer(mahsulot, many=True)
#         return Response(ser.data)
    
#     def post(self, request):
#         ser = MahsulotSer(data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data, status=201)
#         return Response(ser.errors, status=400)


# class MahsulotDetail(APIView):
#     parser_classes = (MultiPartParser, JSONParser)
#     def get(self, request, id):
#         mahsulot = Mahsulot.objects.get(id=id)
#         ser = MahsulotSer(mahsulot)
#         return Response(ser.data)
    
#     def patch(self, request, id):
#         mahsulot = Mahsulot.objects.get(id=id)
#         ser = MahsulotSer(mahsulot, data=request.data, partial=True)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data, status=201)
#         return Response(ser.errors, status=400)
    
#     def delete(self, request, id):
#         mahsulot = Mahsulot.objects.get(id=id)
#         mahsulot.delete()
#         return Response(status=204)


# class XatolarList(APIView):
#     parser_classes = (MultiPartParser, JSONParser)
#     def get(self, request):
#         xatolar = Xatolar.objects.all()
#         ser = XatolarSer(xatolar, many=True)
#         return Response(ser.data)
    
#     def post(self, request):
#         ser = XatolarSer(data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data, status=201)
#         return Response(ser.errors, status=400)


# class XatolarDetail(APIView):
#     parser_classes = (MultiPartParser, JSONParser)
#     def get(self, request, id):
#         xatolar = Xatolar.objects.get(id=id)
#         ser = XatolarSer(xatolar)
#         return Response(ser.data)
    
#     def patch(self, request, id):
#         xatolar = Xatolar.objects.get(id=id)
#         ser = XatolarSer(xatolar, data=request.data, partial=True)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data, status=201)
#         return Response(ser.errors, status=400)
    
#     def delete(self, request, id):
#         xatolar = Xatolar.objects.get(id=id)
#         xatolar.delete()
#         return Response(status=204)


class MissedList(APIView):
    parser_classes = (MultiPartParser, JSONParser)
    def get(self, request):
        missed = Missed.objects.all()
        ser = MissedGetSer(missed, many=True)
        return Response(ser.data)
    
    def post(self, request):
        photo_list = request.data.getlist('photo', [])
        ser = MissedSer(data=request.data)
        if ser.is_valid():
            news = ser.save()
            for x in photo_list:
                p = Photo.objects.create(photo=x)
                news.photo.add(p)
            return Response(ser.data, status=201)
        return Response(ser.errors, status=400)


class MissedDetail(APIView):
    parser_classes = (MultiPartParser, JSONParser)
    def get(self, request, id):
        missed = Missed.objects.get(id=id)
        ser = MissedSer(missed)
        return Response(ser.data)
    
    def patch(self, request, id):
        missed = Missed.objects.get(id=id)
        ser = MissedSer(missed, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=201)
        return Response(ser.errors, status=400)
    
    def delete(self, request, id):
        missed = Missed.objects.get(id=id)
        missed.delete()
        return Response(status=204)
