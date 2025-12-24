from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField




class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18), MaxValueValidator(80)],null=True,blank=True)
    phone_number = PhoneNumberField(null=True,blank=True)
    photo = models.ImageField(upload_to='user_images', null=True, blank=True)
    ROLE_CHOICES = (
    ('client', 'client'),
    ('owner', 'owner'))
    user_role = models.CharField(choices=ROLE_CHOICES, max_length=16, default='client')
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.username}'

class City(models.Model):
    city_image = models.ImageField(upload_to='city_images')
    city_name = models.CharField(max_length=30)


    def __str__(self):
        return f'{self.city_name}'

class Service(models.Model):
    service_image = models.ImageField(upload_to='service_images')
    service_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.service_name

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    postal_code = models.PositiveIntegerField(unique=True, verbose_name="Почта номери")
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='hotels')
    stars = models.PositiveIntegerField(choices=[(i, str(i))for i in range(1, 6)])
    hotel_video = models.FileField(upload_to='hotel_videos')
    description = models.TextField()
    service = models.ManyToManyField(Service)
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.hotel_name

    def get_avg_rating(self):
        ratings = self.hotel_reviews.all()
        if ratings.exists():
            return round(sum([i.stars for i in ratings]) / ratings.count(), 1)
        return 0

    def get_count_people(self):
        return self.hotel_reviews.count()

class HotelImage(models.Model):
    hotel_image = models.ImageField(upload_to='hotel_images')
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_images')

    def __str__(self):
        return f'{self.hotel} - {self.hotel}'

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE,related_name='hotel_rooms')
    room_number = models.PositiveIntegerField()
    ROOM_TYPE_CHOICES = (
    ('стандарт', 'стандарт'),
    ('семейный', 'семейный'))
    room_type = models.CharField(max_length=50, choices= ROOM_TYPE_CHOICES)
    ROOM_STATUS_CHOICES = (
    ('занят', 'занят'),
    ('бронирован', 'бронирован'),
    ('свободен', 'свободен'))
    room_status = models.CharField(max_length=50, choices=ROOM_STATUS_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return f'{self.hotel}, {self.room_number}'


class RoomImage(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='room_images')

    def __str__(self):
        return f'{self.room}, {self.image}'

class Booking(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField()
    check_out = models.DateTimeField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}, {self.hotel}'


class Review(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, related_name='hotel_reviews')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    stars = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}, {self.hotel}'


