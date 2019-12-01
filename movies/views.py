from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets, filters, generics, permissions
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework import mixins
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
import django_filters.rest_framework
from .models import Movie, Classification, Genre, Provider, Profile
from .serializers import MovieSerializer, ProfileSerializer, UserSerializer, ProviderSerializer, ClassificationSerializer, GenreSerializer
from .permissions import IsAdminOrSelf


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["title"]
    renderer_classes = [JSONRenderer]

class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]
    renderer_classes = [JSONRenderer]

class ClassificationViewSet(viewsets.ModelViewSet):
    queryset = Classification.objects.all()
    serializer_class = ClassificationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["text"]
    renderer_classes = [JSONRenderer]

class ProviderViewSet(viewsets.ModelViewSet):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["name"]
    renderer_classes = [JSONRenderer]

class RegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    API endpoint that allows users to created.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        # if the user is admin, return all the users
        if self.request.user.is_superuser:
            return User.objects.all().order_by("-date_joined")
        # if the user is logged in, return only the active user
        if self.request.user:
            return User.objects.filter(pk=self.request.user.pk)
        # if there is no user, return no results
        return User.objects.none()

    @action(methods=["post"], detail=True, permission_classes=[IsAdminOrSelf])
    def set_password(self, request, pk=None):
        """ set the user password """
        serializer = PasswordSerializer(data=request.data)
        user = self.get_object()

        if serializer.is_valid():
            user.set_password(serializer.data.get("new_password"))
            user.save()
            return Response({"status": "password set"})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=["get"], detail=True, permission_classes=[IsAdminOrSelf])
    def reset_password(self, request, pk=None):
        """ set the user password """
        user = self.get_object()
        send_password_reset_email(user)

        return Response({"status": "password reset"}, status=status.HTTP_200_OK)

class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows profiles to be viewed or edited.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticated,)

