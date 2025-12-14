from .models import Country,City,Hotel,Room,Review,Service
from modeltranslation.translator import TranslationOptions,register


@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = ('country_name',)


@register(City)
class CityTranslationOptions(TranslationOptions):
    fields = ('city_name',)


@register(Room)
class RoomTranslationOptions(TranslationOptions):
    fields = ('description',)


@register(Hotel)
class HotelTranslationOptions(TranslationOptions):
    fields = ('hotel_name','street', 'description')


@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = ('text',)


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('service_name',)


