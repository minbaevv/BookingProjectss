import django_filters
from .models import Hotel, Room
from django_filters import FilterSet

from .models import Hotel

class HotelFilter(FilterSet):
    class Meta:
        model = Hotel
        fields = {
            'country': ['exact'],
            'city': ['exact'],
            'stars': ['exact'],
            'service': ['exact'],
        }


class RoomFilter(FilterSet):
    class Meta:
        model = Room
        fields = {
            'room_type': ['exact'],
            'room_status': ['exact'],
            'price': ['gt', 'lt'],
        }