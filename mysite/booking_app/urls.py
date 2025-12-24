from rest_framework import routers
from .views import (
    UserProfileListAPIView, UserProfileDetailAPIView,
    CityListAPIView, CityDetailAPIView, HotelListAPIView, HotelDetailAPIView, RoomViewSet, BookingViewSet,
        ReviewCreateSerializer, ReviewCreateAPIView, ReviewEditAPIView, HotelViewSet, RegisterView, LoginView, LogoutView

)
from django.urls import path, include



router = routers.DefaultRouter()
router.register(r'rooms', RoomViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'hotel_create', HotelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/', UserProfileListAPIView.as_view(), name='users-list'),
    path('users/<int:pk>/', UserProfileDetailAPIView.as_view(),name='user-detail'),
    path('city/', CityListAPIView.as_view(),name='city-list'),
    path('city/<int:pk>/', CityDetailAPIView.as_view(),name='city-detail'),
    path('hotel/', HotelListAPIView.as_view(),name='hotel-list'),
    path('hotel/<int:pk>/', HotelDetailAPIView.as_view(),name='hotel-detail'),
    path('reviews/', ReviewCreateAPIView.as_view(),name='create_review'),
    path('reviews/<int:pk>/', ReviewEditAPIView.as_view(),name='update_review'),
    path('register/', RegisterView.as_view(),name='register'),
    path('login/', LoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(),name='logout'),
]
