from django.urls import path
from django.contrib.auth import views as auth_views

from .views import SignUp, XodimList, XodimDetail, Userdetail, ChangePasswordView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


app_name='user'
urlpatterns = [
    path('change/', ChangePasswordView.as_view(), name='change_pass'),
    path('signup/<int:id>/', Userdetail.as_view(), name='userdetail'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('change-password/', auth_views.PasswordChangeView.as_view()),
    path('xodim/', XodimList.as_view(), name='xodim'),
    path('xodim/<int:id>/', XodimDetail.as_view(), name='xodim_detail'),
]
