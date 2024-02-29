from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from .models import User
from Post.models import Xodim


class ChangePasswordSerializer(serializers.Serializer):
    model = User

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


class MyTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        data = super(MyTokenRefreshSerializer, self).validate(attrs)
        data['refresh'] = attrs['refresh']
        return data


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super(MyTokenObtainPairSerializer, self).validate(attrs)
        user = User.objects.get(username=self.user.username)
        data['status'] = user.status
        data['id'] = user.id
        data['gender'] = user.gender
        return data


class UserSer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=16, write_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'photo', 'phone', 'status', 'gender')

    def create(self, validated_data):
        user = super().create(self.validated_data)
        user.set_password(validated_data.pop('password', None))
        user.save()
        return user
    
    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.phone = validated_data.get('phone', instance.phone)
        # instance.status = validated_data.get('status', instance.status)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.save()
        return instance


class XodimSer(serializers.ModelSerializer):
    class Meta:
        model = Xodim
        fields = ('id', 'first_name', 'last_name', 'photo', 'phone', 'ish_turi', 'id_raqam', 'gender', 'bulimi')
    
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.bulimi = validated_data.get('bulimi', instance.bulimi)
        instance.id_raqam = validated_data.get('id_raqam', instance.id_raqam)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.save()
        return instance