from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.fields import DateField
from .models import (
    UserProfile, City, Service, Hotel, HotelImage, Room, RoomImage, Booking, Review, Country
)
from rest_framework_simplejwt.tokens import RefreshToken



class UserProfileRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password',
                  'age', 'phone_number', )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }





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

class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['stars', 'text', 'user', 'hotel']

class ReviewSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format='%d.%m.%Y %H:%M')
    user = UserProfileReviewSerializer(read_only=True)
    class Meta:
        model = Review
        fields = ('id', 'user', 'text','created_date')

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

class HotelCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('__all__')