from .models import Movie, Classification, Genre, Provider
from rest_framework import serializers

class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']

class ClassificationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Classification
        fields = ['text']

class ProviderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Provider
        fields = ['name', 'url']

class MovieSerializer(serializers.HyperlinkedModelSerializer):
    provider = ProviderSerializer (many=True)
    genre = GenreSerializer (many=True)
    classification = ClassificationSerializer (read_only=True)
    
    class Meta:
        model = Movie
        fields = ['title', 'summary', 'duration', 'release_date', 'provider', 'genre', 'classification']
