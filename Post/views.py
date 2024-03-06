from django.shortcuts import render
from django.db.models import Q, F, Count, Sum, Min, Max

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.parsers import MultiPartParser, JSONParser

from .serializers import (PhotoSer, Ish_TuriSer, BulimSer, MahsulotSer,
                          XatolarSer, MissedSer, MissedGetSer)
from .models import (Photo, Ish_Turi, Bulim, Xodim, Mahsulot, Xatolar, Missed)
from User.models import User


from datetime import datetime, timedelta
from django.utils import timezone


# class Maxsulot(APIView):
#     parser_classes = [JSONParser, MultiPartParser]
#     def get(self, request):
#         xodim = Xodim.objects.all()
#         l = []
#         for x in xodim:
#             missed = Missed.objects.filter(xodim=x)
#             sum_xato = missed.aggregate(Sum('xato_soni'))
#             sum_butun = missed.aggregate(Sum('butun_soni'))
#             # xatosi = missed.aggregate(Count('xato'))
#             # for k in missed:
#             l.append({
#                 'name': x.missed_xodim.mahsulot.name,
#                 'xodimi': x.first_name,
#                 'xato_soni': sum_xato,
#                 'butun_soni': sum_butun,
#                 # 'xato': xatosi
#             })
#         return Response(l)



# class XodimStatistic(APIView):
#     parser_classes = [JSONParser, MultiPartParser]
#     def get(self, request):
        # xodim = Xodim.objects.all()
        # l = []
        # for x in xodim:
        #     missed = Missed.objects.filter(xodim=x)
        #     for k in missed:
        #         d = {}
        #         d['name'] = x.first_name
        #         d['ish_vaqti'] = k.ish_vaqti
        #         for 
        #         d['xato_soni'] = k.xato_soni
            


class XodimStatistic(APIView):
    parser_classes = [JSONParser, MultiPartParser]

    def get(self, request):
        xozir = timezone.now()
        
        bir_yil_oldin = xozir - timedelta(days=365)
        olti_oy_oldin = xozir - timedelta(days=30*6)
        bir_oy_oldin = xozir - timedelta(days=30)
        bir_xafta_oldin = xozir - timedelta(days=7)
        bir_kun_oldin = xozir - timedelta(days=1)

        statistics = []

        def statistika(start_date, end_date):
            xodimlar = Xodim.objects.all()
            data = []
            for x in xodimlar:
                missed = Missed.objects.filter(xodim=x, created_at__range=[start_date, end_date])
                total_ish_vaqti = 0
                total_xato_soni = 0
                total_butun_soni = 0
                for hisobot in missed:
                    total_ish_vaqti += hisobot.ish_vaqti
                    total_xato_soni += hisobot.xato_soni
                    total_butun_soni += hisobot.butun_soni
                data.append({
                    'ism': x.first_name,
                    'ish_vaqti': total_ish_vaqti,
                    'xato_soni': total_xato_soni,
                    'butun_soni': total_butun_soni
                })
            return data

        # Calculate statistics for different time periods and append to the statistics list
        statistics.append({'period': '1 year', 'data': statistika(bir_yil_oldin, xozir)})
        statistics.append({'period': '6 months', 'data': statistika(olti_oy_oldin, xozir)})
        statistics.append({'period': '1 month', 'data': statistika(bir_oy_oldin, xozir)})
        statistics.append({'period': '1 week', 'data': statistika(bir_xafta_oldin, xozir)})
        statistics.append({'period': '1 day', 'data': statistika(bir_kun_oldin, xozir)})

        return Response(statistics)


# class StatisticView(APIView):
#     def get(self, request):




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
            status_b = ser.validated_data['user']
            print(status_b)
            ser.save()
            return Response(ser.data, status=201)
        return Response(ser.errors, status=400)


class BulimDetail(APIView):
    parser_classes = (MultiPartParser, JSONParser)
    def get(self, request, id):
        bulim = Bulim.objects.get(id=id)
        ser = BulimSer(bulim)
        a = {}
        if Missed.objects.filter(xodim__bulimi=bulim):
            missed = Missed.objects.filter(xodim__bulimi=bulim)
            sum_xato = missed.aggregate(soni=Sum('xato_soni'))
            sum_butun = missed.aggregate(soni=Sum('butun_soni'))
            a[str('bulim_name')]=str(bulim.name)
            a[str('bulim_id')]=str(bulim.bulim_id)
            a[str('bulim_boshliq')]=str(bulim.user.first_name)
            a[str('xato_soni')]=sum_xato
            a[str('butun_soni')]=sum_butun
            a[str('hisobot_soni')]=len(missed)
            b = missed.aggregate(Count('xodim'))
            a[str('xodim_soni')]=b

            c = []
            for j in missed:
                print(j)
                found = False
                for item in c:
                    if item['mahsulot_name'] == j.mahsulot.name:
                        item['mahsulot_id'] += j.mahsulot.mahsulot_id
                        item['xato_soni'] += j.xato_soni
                        item['butun_soni'] += j.butun_soni
                        found = True
                        break
                if not found:
                    c.append({'mahsulot_name': j.mahsulot.name, 'mahsulot_id': j.mahsulot.mahsulot_id, 'xato_soni': j.xato_soni, 'butun_soni': j.butun_soni})

            d = []
            for j in missed:
                print(j)
                found = False
                for item in d:
                    if item['xato_name'] == j.xato.name:
                        item['xato_id'] = j.xato.xato_id
                        item['mahsulot_name'] = j.mahsulot.name
                        item['xato_soni'] += j.xato_soni
                        found = True
                        break
                if not found:
                    d.append({'xato_name': j.xato.name, 'xato_id': j.xato.xato_id, 'mahsulot_name': j.mahsulot.name, 'xato_soni': j.xato_soni})
            return Response({'data':ser.data,
                         'statistic':a,
                         'mahsulot':c,
                         'xato': d

                         })
        return Response({'data':ser.data,
                         'statistic':None,
                         'mahsulot':None,
                         'xato': None
                         })
    
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
    parser_classes = [MultiPartParser, JSONParser]
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
    parser_classes = [MultiPartParser, JSONParser]
    def get(self, request, id):
        missed = Missed.objects.get(id=id)
        ser = MissedSer(missed)
        return Response(ser.data)
    
    def patch(self, request, id):
        photo_list = request.data.getlist('photo')
        missed = Missed.objects.get(id=id)
        ser = MissedSer(missed, data=request.data, partial=True)
        if ser.is_valid():
            news = ser.save()
            if photo_list:
                for x in photo_list:
                    p = Photo.objects.create(photo=x)
                    news.photo.add(p)
            return Response(ser.data, status=201)
        return Response(ser.errors, status=400)
    
    def delete(self, request, id):
        missed = Missed.objects.get(id=id)
        missed.delete()
        return Response(status=204)
