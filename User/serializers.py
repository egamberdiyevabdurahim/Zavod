from rest_framework import serializers

from .models import User
from Post.models import Xodim


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


class XodimSer(serializers.ModelSerializer):
    class Meta:
        model = Xodim
        fields = ('id', 'first_name', 'last_name', 'photo', 'phone', 'ish_turi', 'id_raqam', 'gender')