from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.fields import DateField
from .models import (
    UserProfile, City, Service, Hotel, HotelImage, Room, RoomImage, Booking, Review, Country
)

class UserProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id','photo','first_name', 'last_name','user_role']


class UserProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_image']

class HotelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelImage
        fields = ['hotel_image']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['service_image', 'service_name']

class CitySimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['city_name']

class CountryReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_image','country_name']

class UserProfileReviewSerializer(serializers.ModelSerializer):
    country = CountryReviewSerializer()
    class Meta:
        model = UserProfile
        fields = ['photo','first_name','country' ]


class HotelListSerializer(serializers.ModelSerializer):
    city = CitySimpleSerializer()
    hotel_images = HotelImageSerializer(many=True, read_only=True)
    avg_rating = serializers.SerializerMethodField()
    count_people = serializers.SerializerMethodField()

    class Meta:
        model = Hotel
        fields = ['id','hotel_images','hotel_name', 'stars', 'city', 'description', 'avg_rating','count_people']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()
    def get_count_people(self,obj):
        return obj.get_count_people()


class CountryNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']


class CityListSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    class Meta:
        model = City
        fields = ['id','city_name','city_image', 'country', ]



class CityDetailSerializer(serializers.ModelSerializer):
    hotels = HotelListSerializer(many=True, read_only=True)
    class Meta:
        model = City
        fields = ['city_name', 'hotels']


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'user_role']




class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['room_type','description']

class RoomImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomImage
        fields = ('__all__')

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('__all__')



class ReviewSerializer(serializers.ModelSerializer):
    user = UserProfileReviewSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ('id', 'user', 'text')

class HotelDetailSerializer(serializers.ModelSerializer):
    hotel_images = HotelImageSerializer(many=True, read_only=True)
    city = CitySimpleSerializer()
    country = CountryNameSerializer()
    service = ServiceSerializer(many=True)
    owner = OwnerSerializer()
    hotel_rooms = RoomSerializer(many=True)
    hotel_reviews = ReviewSerializer(many=True, read_only=True)
    avg_rating = serializers.SerializerMethodField()
    count_people = serializers.SerializerMethodField()
    class Meta:
        model = Hotel
        fields = ['hotel_name','street','postal_code', 'stars',
                  'city','country','hotel_video','hotel_images','description', 'service',
                  'owner','hotel_rooms','hotel_reviews', 'avg_rating','count_people']

    def get_avg_rating(self, obj):
        return obj.get_avg_rating()
    def get_count_people(self,obj):
        return obj.get_count_people()
