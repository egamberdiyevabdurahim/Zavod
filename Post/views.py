from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, JSONParser

from .serializers import *
from .models import *


class PhotoEditView(APIView):
    def patch(self, request, id):
        photo = Photo.objects.get(id=id)
        rasm = request.data.get('photo')
        photo.photo = rasm
        photo.save()
        return Response({})


class PhotoList(APIView):
    parser_classes = (MultiPartParser, JSONParser)
    def get(self, request):
        photos = Photo.objects.all()
        ser = PhotoSer(photos, many=True)
        return Response(ser.data)
    
    def post(self, request):
        ser = PhotoSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=201)
        return Response(ser.errors, status=400)


class IshTuriList(APIView):
    parser_classes = (MultiPartParser, JSONParser)
    def get(self, request):
        ishturi = Ish_Turi.objects.all()
        ser = Ish_TuriSer(ishturi, many=True)
        return Response(ser.data)
    
    def post(self, request):
        ser = Ish_TuriSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=201)
        return Response(ser.errors, status=400)


class Ish_TuriDetail(APIView):
    parser_classes = (MultiPartParser, JSONParser)
    def get(self, request, id):
        ishturi = Ish_Turi.objects.get(id=id)
        ser = Ish_TuriSer(ishturi)
        return Response(ser.data)
    
    def patch(self, request, id):
        ishturi = Ish_Turi.objects.get(id=id)
        ser = Ish_TuriSer(ishturi, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=201)
        return Response(ser.errors, status=400)
    
    def delete(self, request, id):
        ishturi = Ish_Turi.objects.get(id=id)
        ishturi.delete()
        return Response(status=204)


class BulimList(APIView):
    parser_classes = (MultiPartParser, JSONParser)
    def get(self, request):
        bulim = Bulim.objects.all()
        ser = BulimSer(bulim, many=True)
        return Response(ser.data)
    
    def post(self, request):
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


class MahsulotList(APIView):
    parser_classes = (MultiPartParser, JSONParser)
    def get(self, request):
        mahsulot = Mahsulot.objects.all()
        ser = MahsulotSer(mahsulot, many=True)
        return Response(ser.data)
    
    def post(self, request):
        ser = MahsulotSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=201)
        return Response(ser.errors, status=400)


class MahsulotDetail(APIView):
    parser_classes = (MultiPartParser, JSONParser)
    def get(self, request, id):
        mahsulot = Mahsulot.objects.get(id=id)
        ser = MahsulotSer(mahsulot)
        return Response(ser.data)
    
    def patch(self, request, id):
        mahsulot = Mahsulot.objects.get(id=id)
        ser = MahsulotSer(mahsulot, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=201)
        return Response(ser.errors, status=400)
    
    def delete(self, request, id):
        mahsulot = Mahsulot.objects.get(id=id)
        mahsulot.delete()
        return Response(status=204)


class XatolarList(APIView):
    parser_classes = (MultiPartParser, JSONParser)
    def get(self, request):
        xatolar = Xatolar.objects.all()
        ser = XatolarSer(xatolar, many=True)
        return Response(ser.data)
    
    def post(self, request):
        ser = XatolarSer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=201)
        return Response(ser.errors, status=400)


class XatolarDetail(APIView):
    parser_classes = (MultiPartParser, JSONParser)
    def get(self, request, id):
        xatolar = Xatolar.objects.get(id=id)
        ser = XatolarSer(xatolar)
        return Response(ser.data)
    
    def patch(self, request, id):
        xatolar = Xatolar.objects.get(id=id)
        ser = XatolarSer(xatolar, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=201)
        return Response(ser.errors, status=400)
    
    def delete(self, request, id):
        xatolar = Xatolar.objects.get(id=id)
        xatolar.delete()
        return Response(status=204)


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
        a = request.data.get('photo',None)
        missed = Missed.objects.get(id=id)
        ser = MissedSer(missed, data=request.data, partial=True)
        if ser.is_valid():
            news = ser.save()
            if a:
                for x in a:
                    new_photo = Photo.objects.create(photo=x)
                    news.photo.add(new_photo)
            # instance.photo.remove(validated_data.get('photo', instance.photo))
        
            # a = request.data.get('photo',None)
            # if a:
            #     for x in a:
            #         new_photo = Photo.objects.create(photo=x)
            #         c.photo.add(new_photo)
            #         c.photo.remove(request.data.get('photo'))
            return Response(ser.data, status=201)
        return Response(ser.errors, status=400)
    
    def delete(self, request, id):
        missed = Missed.objects.get(id=id)
        missed.delete()
        return Response(status=204)
