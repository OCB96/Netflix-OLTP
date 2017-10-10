from rest_framework import serializers
from .models import User, Zip, Access, Plans, Payment, User_Rentals, Rentals, Content, Type, Genre, Ratings, Director, Cast


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'user_name', 'user_email', 'zip_id', 'user_country', 'user_phone', 'plan_id', 'created_at', 'updated_at')


class ZipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zip
        fields = ('zip_id', 'state', 'street', 'city')


class AccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Access
        fields = ('user_name', 'user_id', 'user_pass')


class PlansSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plans
        fields = ('plan_id', 'plan_desc', 'plan_price')


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('payment_id', 'payment_date', 'plan_id', 'user_id')


class User_RentalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User_Rentals
        fields = ('user_rental_id', 'user_id', 'rental_id')


class RentalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rentals
        fields = ('rental_id', 'stream_date', 'stream_length', 'content_id')


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('content_id', 'title', 'content_type', 'release_year', 'director_id', 'cast_id', 'genre_id', 'type_id')


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ('type_id', 'type_desc')


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('genre_id', 'genre_desc')


class RatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ratings
        fields = ('ratings_id', 'video_quality', 'audio_quality', 'subtitle_quality', 'user_id', 'content_id')


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ('director_id', 'director_name')


class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = ('cast_id', 'cast_name')
