from utility.views import BaseListView, BaseDetailsView, BaseSearchView
from app_auth import models, serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTStatelessUserAuthentication

from rest_framework_simplejwt.views import TokenObtainPairView


class UserListView(BaseListView):
    model = models.User
    serializer = serializers.UserSerializer
    authentication_classes = []
    permission_classes = []


class UserDetailsView(BaseDetailsView):
    model = models.User
    serializer = serializers.UserSerializer
    authentication_classes = [JWTStatelessUserAuthentication]
    permission_classes = [IsAuthenticated]


class UserSearchView(BaseSearchView):
    model = models.User
    serializer = serializers.UserSerializer
    authentication_classes = [JWTStatelessUserAuthentication]
    permission_classes = [IsAuthenticated]


class LoginView(TokenObtainPairView):
    name = "The login endpoint"
    serializer_class = serializers.LoginSerializer
    authentication_classes = []
    permission_classes = []

