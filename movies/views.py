from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets, filters, generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer
from django.contrib.auth.models import User
import django_filters.rest_framework
from .models import Movie, Classification, Provider, Genre
from .serializers import MovieSerializer, GenreSerializer, ProviderSerializer, ClassificationSerializer, UserSerializer, ProfileSerializer
from .models import Profile
from .permissions import IsAdminOrSelf, IsAdminUser


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

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_permissions(self):
        permission_classes=[]
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAdminOrSelf]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    # permission_classes = (IsAuthenticated,)