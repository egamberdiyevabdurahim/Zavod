from django.urls import path

from .views import SignUp, XodimList, XodimDetail

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


app_name='user'
urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('xodim/', XodimList.as_view(), name='xodim'),
    path('xodim/<int:id>/', XodimDetail.as_view(), name='xodim_detail'),
]
