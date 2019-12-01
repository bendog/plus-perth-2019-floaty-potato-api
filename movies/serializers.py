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
        fields = ["date_of_birth"]

class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = ProfileSerializer(many=False, required=True)

    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'first_name', 'password', 'last_name','profile']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        Profile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()

        profile.date_of_birth = profile_data.get('date_of_birth', profile.date_of_birth)
        profile.save()

        return instance