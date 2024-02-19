from django.urls import path

from .views import *


urlpatterns = [
    path('photo/', PhotoList.as_view(), name='photo'),
    path('ish_turi/', IshTuriList.as_view(), name='ish_turi'),
    path('ish_turi/<int:id>', Ish_TuriDetail.as_view(), name='ish_turi_detail'),
    path('bulim/', BulimList.as_view(), name='bulim'),
    path('bulim/<int:id>', BulimDetail.as_view(), name='bulim_detail'),
    path('mahsulot/', MahsulotList.as_view(), name='mahsulot'),
    path('mahsulot/<int:id>', MahsulotDetail.as_view(), name='mahsulot_detail'),
    path('xatolar/', XatolarList.as_view(), name='xatolar'),
    path('xatolar/<int:id>', XatolarDetail.as_view(), name='xatolar_detail'),
    path('missed/', MissedList.as_view(), name='missed'),
    path('missed/<int:id>', MissedDetail.as_view(), name='missed_detail'),
]