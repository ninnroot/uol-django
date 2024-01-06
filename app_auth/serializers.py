from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from app_auth.models import User
from utility.serializers import BaseModelSerializer, BaseSerializer


class UserSerializer(BaseModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}
        expandable_fields = {
        }

    def create(self, validated_data):
        password = validated_data.pop("password")

        user = super().create(validated_data)
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.save()

        return user


class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        del data["refresh"]
        data["user"] = UserSerializer(self.user).data
        return data
