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
        fields = ['id', 'url', 'username', 'email', 'password', 'first_name', 'last_name', 'profile']

    def create(self, validated_data):
        User
        validated_data['is_active'] = False
        # validated_data['password'] = self.context.get('request').password
        # print('data:', validated_data )
        user = User(**validated_data)
        user.save()
        user.set_password(validated_data.get('password'))
        return user

class PasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """

    new_password = serializers.CharField(required=True)