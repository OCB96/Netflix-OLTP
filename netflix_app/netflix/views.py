from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import User, Zip, Access, Plans, Payment, User_Rentals, Rentals, Content, Type, Genre, Ratings, Director, Cast
from .serializers import UserSerializer, ZipSerializer, AccessSerializer, PlansSerializer, PaymentSerializer, User_RentalsSerializer, RentalsSerializer, ContentSerializer, TypeSerializer, GenreSerializer, RatingsSerializer, DirectorSerializer, CastSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class ZipViewSet(ModelViewSet):
    serializer_class = ZipSerializer
    queryset = Zip.objects.all()


class AccessViewSet(ModelViewSet):
    serializer_class = AccessSerializer
    queryset = Access.objects.all()


class PlansViewSet(ModelViewSet):
    serializer_class = PlansSerializer
    queryset = Plans.objects.all()


class PaymentViewSet(ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()


class User_RentalsViewSet(ModelViewSet):
    serializer_class = User_RentalsSerializer
    queryset = User_Rentals.objects.all()


class RentalsViewSet(ModelViewSet):
    serializer_class = RentalsSerializer
    queryset = Rentals.objects.all()


class ContentViewSet(ModelViewSet):
    serializer_class = ContentSerializer
    queryset = Content.objects.all()


class TypeViewSet(ModelViewSet):
    serializer_class = TypeSerializer
    queryset = Type.objects.all()


class GenreViewSet(ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()


class RatingsViewSet(ModelViewSet):
    serializer_class = RatingsSerializer
    queryset = Ratings.objects.all()


class DirectorViewSet(ModelViewSet):
    serializer_class = DirectorSerializer
    queryset = Director.objects.all()


class CastViewSet(ModelViewSet):
    serializer_class = CastSerializer
    queryset = Cast.objects.all()
