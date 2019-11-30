from .models import Movie, Classification, Genre, Provider, Profile
from rest_framework import serializers
from django.contrib.auth.models import User

class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = ['name', 'image']

class ClassificationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Classification
        fields = ['text', 'image']

class ProviderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Provider
        fields = ['name', 'url', 'image']

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    provider = ProviderSerializer (many=True)
    genre = GenreSerializer (many=True)
    classification = ClassificationSerializer (read_only=True)
    
    class Meta:
        model = Movie
        fields = ['title', 'summary', 'duration', 'release_date', 'image', 'provider', 'genre', 'classification']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(many=False, required=False)
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'first_name', 'last_name','profile']