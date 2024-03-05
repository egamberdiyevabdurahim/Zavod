from django.shortcuts import render
from django.db.models import Q, F, Sum, Min, Max

from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, UpdateAPIView
from rest_framework.parsers import MultiPartParser, JSONParser
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from Post.models import Ish_Turi, Mahsulot, Xodim, Missed
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
                             'access_token': access,
                             'refresh_token': str(refresh)
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


class XodimList(APIView):
    parser_classes = [MultiPartParser, JSONParser]
    def get(self, request):
        xodim = Xodim.objects.all()
        ser = XodimSer(xodim, many=True)
        # l = []
        # for x in xodim:
        #     missed = Missed.objects.filter(xodim=x)
            
        #     print(missed)
        #     xato_sonii = missed.aaggregate(Sum('xato_soni'))
        #     butun_sonii = missed.aaggregate(Sum('butun_soni'))
        #     # mahsulot = missed.mahsulot
        #     for i in missed:
        #         l.append({
        #         # 'id': x.id,
        #         'name': x.first_name,
        #         'xato_soni': i.xato_soni,
        #         'butun_soni': i.butun_soni
        #         })
        return Response({'data':ser.data, 
                        })
    
    def post(self, request):
        ish_list = request.data.getlist('ish_turi', [])
        ser = XodimSer(data=request.data)
        if ser.is_valid():
            ser.save()
            # news = ser.save()
            # for x in ish_list:
            #     p = Ish_Turi.objects.create(name=x)
            #     news.ish_turi.add(p)
            return Response(ser.data)
        return Response(ser.errors)


class XodimDetail(APIView):
    parser_classes = [MultiPartParser, JSONParser]
    def get(self, request, id):
        try:
            xodim = Xodim.objects.get(id=id)
            ser = XodimSer(xodim)
            p = []
            d={}
            missed = Missed.objects.filter(xodim=xodim)
            sum_xato = missed.aggregate(Sum('xato_soni'))
            sum_butun = missed.aggregate(Sum('butun_soni'))
            sum_mah_xato = missed.aggregate(Sum('mahsulot'))
            d['sum_mah'] = sum_mah_xato
            for i in missed:
                p.append({
                'name': xodim.first_name,
                'mahsulot_name': i.mahsulot.name,
                'xato_soni': i.xato_soni,
                'butun_soni': i.butun_soni,
                })
            return Response({'data':ser.data,
                             'statistic': p,
                             'dd': d})
        except:
            return Response({'xato':'bu id xato'})
    
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


class XodimDetail(APIView):
    parser_classes = [JSONParser, MultiPartParser]
    def get(self, request, id):
        # try:
        xodim = Xodim.objects.get(id=id)
        ser = XodimSer(xodim)
        p=[]
        s=[]
        h = Missed.objects.filter(xodim=xodim)
        sum_xato = h.aggregate(soni=Sum('xato_soni'))
        sum_butun = h.aggregate(soni=Sum('butun_soni'))
        s.append({
            'id': xodim.id,
            'xodimi': xodim.first_name,
            'Jami_xato': sum_xato,
            'Jami_butun': sum_butun,
        })
        d={}
        for j in h:
            xodim_mistakes = Missed.objects.filter(xodim=j.xodim, mahsulot=j.mahsulot)
            xodim_mistakes_aggregated = xodim_mistakes.aggregate(total_xato_soni=Sum('xato_soni'))
            d[str(j.mahsulot.name)] = xodim_mistakes_aggregated['total_xato_soni']
        
        k = []
        for j in h:
            found = False
            for item in k:
                if item['mahsulot_name'] == j.mahsulot.name:
                    item['xato_soni'] += j.xato_soni
                    item['butun_soni'] += j.butun_soni
                    found = True
                    break
            if not found:
                k.append({'mahsulot_name': j.mahsulot.name, 'xato_soni': j.xato_soni, 'butun_soni': j.butun_soni})
        return Response({'data':ser.data,
                        'all_statistic': s,
                        'mahsulot_xato_soni':d,
                        'statistic':k,
                        })
        # except:
            # return Response({'xato': "bu id xato"})
