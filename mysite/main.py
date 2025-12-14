import os
import django
import random
from datetime import datetime, timedelta, date
from decimal import Decimal

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.contrib.auth.hashers import make_password
from booking_app.models import (
    Country, UserProfile, City, Service, Hotel,
    HotelImage, Room, RoomImage, Booking, Review
)


def clear_data():
    """Очистка всех данных"""
    print("Очистка базы данных...")
    Review.objects.all().delete()
    Booking.objects.all().delete()
    RoomImage.objects.all().delete()
    Room.objects.all().delete()
    HotelImage.objects.all().delete()
    Hotel.objects.all().delete()
    Service.objects.all().delete()
    City.objects.all().delete()
    UserProfile.objects.all().delete()
    Country.objects.all().delete()
    print("База данных очищена")


def populate_countries():
    """Создание стран"""
    print("Создание стран...")

    countries_data = [
        {'en': 'Kyrgyzstan', 'ru': 'Кыргызстан'},
        {'en': 'Kazakhstan', 'ru': 'Казахстан'},
        {'en': 'Uzbekistan', 'ru': 'Узбекистан'},
        {'en': 'Turkey', 'ru': 'Турция'},
        {'en': 'United Arab Emirates', 'ru': 'ОАЭ'},
        {'en': 'Russia', 'ru': 'Россия'},
        {'en': 'Georgia', 'ru': 'Грузия'},
        {'en': 'Thailand', 'ru': 'Таиланд'},
        {'en': 'Italy', 'ru': 'Италия'},
        {'en': 'France', 'ru': 'Франция'}
    ]

    countries = []
    for country_data in countries_data:
        country = Country.objects.create(
            country_name_en=country_data['en'],
            country_name_ru=country_data['ru'],
            country_image=f'country_images/{country_data["en"].lower().replace(" ", "_")}.png'
        )
        countries.append(country)

    print(f"Создано {len(countries)} стран")
    return countries


def populate_cities(countries):
    """Создание городов"""
    print("Создание городов...")

    cities_data = {
        'Kyrgyzstan': [
            {'en': 'Bishkek', 'ru': 'Бишкек'},
            {'en': 'Osh', 'ru': 'Ош'},
            {'en': 'Issyk-Kul', 'ru': 'Иссык-Куль'},
            {'en': 'Karakol', 'ru': 'Каракол'}
        ],
        'Kazakhstan': [
            {'en': 'Almaty', 'ru': 'Алматы'},
            {'en': 'Astana', 'ru': 'Астана'},
            {'en': 'Shymkent', 'ru': 'Шымкент'}
        ],
        'Uzbekistan': [
            {'en': 'Tashkent', 'ru': 'Ташкент'},
            {'en': 'Samarkand', 'ru': 'Самарканд'},
        ],
        'Turkey': [
            {'en': 'Istanbul', 'ru': 'Стамбул'},
            {'en': 'Antalya', 'ru': 'Анталья'},
            {'en': 'Ankara', 'ru': 'Анкара'}
        ],
        'United Arab Emirates': [
            {'en': 'Dubai', 'ru': 'Дубай'},
            {'en': 'Abu Dhabi', 'ru': 'Абу-Даби'}
        ],
        'Russia': [
            {'en': 'Moscow', 'ru': 'Москва'},
            {'en': 'Saint Petersburg', 'ru': 'Санкт-Петербург'}
        ],
        'Georgia': [
            {'en': 'Tbilisi', 'ru': 'Тбилиси'},
            {'en': 'Batumi', 'ru': 'Батуми'}
        ],
        'Thailand': [
            {'en': 'Bangkok', 'ru': 'Бангкок'},
            {'en': 'Phuket', 'ru': 'Пхукет'}
        ],
        'Italy': [
            {'en': 'Rome', 'ru': 'Рим'},
            {'en': 'Venice', 'ru': 'Венеция'}
        ],
        'France': [
            {'en': 'Paris', 'ru': 'Париж'},
            {'en': 'Nice', 'ru': 'Ницца'}
        ]
    }

    cities = []
    for country in countries:
        country_name_en = country.country_name_en
        if country_name_en in cities_data:
            for city_data in cities_data[country_name_en]:
                city = City.objects.create(
                    country=country,
                    city_name_en=city_data['en'],
                    city_name_ru=city_data['ru'],
                    city_image=f'city_images/{city_data["en"].lower()}.png'
                )
                cities.append(city)

    print(f"Создано {len(cities)} городов")
    return cities


def populate_services():
    """Создание услуг"""
    print("Создание услуг...")

    services_data = [
        {'en': 'Free WiFi', 'ru': 'Бесплатный WiFi'},
        {'en': 'Swimming Pool', 'ru': 'Бассейн'},
        {'en': 'Spa & Wellness', 'ru': 'Спа и велнес'},
        {'en': 'Restaurant', 'ru': 'Ресторан'},
        {'en': 'Free Parking', 'ru': 'Бесплатная парковка'},
        {'en': 'Fitness Center', 'ru': 'Фитнес-центр'},
        {'en': 'Conference Room', 'ru': 'Конференц-зал'},
        {'en': 'Airport Transfer', 'ru': 'Трансфер из аэропорта'},
        {'en': 'Room Service 24/7', 'ru': 'Обслуживание номеров 24/7'},
        {'en': 'Pet Friendly', 'ru': 'Можно с питомцами'}
    ]

    services = []
    for service_data in services_data:
        service = Service.objects.create(
            service_name_en=service_data['en'],
            service_name_ru=service_data['ru'],
            service_image=f'service_images/{service_data["en"].lower().replace(" ", "_")}.png'
        )
        services.append(service)

    print(f"Создано {len(services)} услуг")
    return services


def populate_users(countries):
    """Создание пользователей"""
    print("Создание пользователей...")

    # Клиенты
    clients_data = [
        {'first': 'John', 'last': 'Smith', 'username': 'johnsmith', 'age': 32, 'phone': '+996555111222'},
        {'first': 'Emma', 'last': 'Johnson', 'username': 'emmaj', 'age': 28, 'phone': '+996777222333'},
        {'first': 'Michael', 'last': 'Brown', 'username': 'mikebrown', 'age': 35, 'phone': '+996700333444'},
        {'first': 'Sophia', 'last': 'Davis', 'username': 'sophiad', 'age': 29, 'phone': '+996555444555'},
        {'first': 'Daniel', 'last': 'Wilson', 'username': 'danwilson', 'age': 41, 'phone': '+996770555666'},
    ]

    # Владельцы отелей
    owners_data = [
        {'first': 'Alexander', 'last': 'Petrov', 'username': 'alexpetrov', 'age': 45, 'phone': '+996555666777'},
        {'first': 'Victoria', 'last': 'Ivanova', 'username': 'vickyivanov', 'age': 38, 'phone': '+996777777888'},
        {'first': 'Dmitry', 'last': 'Sokolov', 'username': 'dmitrysokolov', 'age': 42, 'phone': '+996700888999'},
        {'first': 'Elena', 'last': 'Kozlova', 'username': 'elenakozlova', 'age': 40, 'phone': '+996555999000'},
        {'first': 'Sergey', 'last': 'Morozov', 'username': 'sergeymorozov', 'age': 50, 'phone': '+996770000111'},
    ]

    clients = []
    owners = []

    for i, client_data in enumerate(clients_data, 1):
        client = UserProfile.objects.create(
            username=client_data['username'],
            email=f'client{i}@example.com',
            password=make_password('password123'),
            first_name=client_data['first'],
            last_name=client_data['last'],
            age=client_data['age'],
            phone_number=client_data['phone'],
            country=random.choice(countries),
            user_role='client',
            photo=f'user_images/client{i}.png'
        )
        clients.append(client)

    for i, owner_data in enumerate(owners_data, 1):
        owner = UserProfile.objects.create(
            username=owner_data['username'],
            email=f'owner{i}@example.com',
            password=make_password('password123'),
            first_name=owner_data['first'],
            last_name=owner_data['last'],
            age=owner_data['age'],
            phone_number=owner_data['phone'],
            country=random.choice(countries),
            user_role='owner',
            photo=f'user_images/owner{i}.png'
        )
        owners.append(owner)

    print(f"Создано {len(clients)} клиентов и {len(owners)} владельцев")
    return clients, owners


def populate_hotels(cities, services, owners):
    """Создание отелей"""
    print("Создание отелей...")

    hotels_data = [
        {
            'name_en': 'Grand Plaza Hotel',
            'name_ru': 'Гранд Плаза Отель',
            'street_en': '123 Main Street',
            'street_ru': 'Главная улица, 123',
            'desc_en': 'Luxury 5-star hotel in the heart of the city. Features elegant rooms, rooftop restaurant, spa center, and panoramic city views. Perfect for business and leisure travelers.',
            'desc_ru': 'Роскошный 5-звездочный отель в самом центре города. Элегантные номера, ресторан на крыше, спа-центр и панорамный вид на город. Идеально для деловых и туристических поездок.',
            'stars': 5,
            'postal': 720000
        },
        # ... (оставил остальные элементы без изменений для краткости)
        {
            'name_en': 'Family Garden Hotel',
            'name_ru': 'Фэмили Гарден Отель',
            'street_en': '741 Park Lane',
            'street_ru': 'Парковая аллея, 741',
            'desc_en': 'Family-oriented hotel with spacious suites. Kids playground, family pool, babysitting service, and children\'s menu. Safe and comfortable environment.',
            'desc_ru': 'Семейный отель с просторными номерами. Детская площадка, семейный бассейн, услуги няни и детское меню. Безопасная и комфортная обстановка.',
            'stars': 3,
            'postal': 720009
        }
    ]

    hotels = []
    for i, hotel_data in enumerate(hotels_data):
        city = random.choice(cities)
        hotel = Hotel.objects.create(
            hotel_name_en=hotel_data['name_en'],
            hotel_name_ru=hotel_data['name_ru'],
            street_en=hotel_data['street_en'],
            street_ru=hotel_data['street_ru'],
            postal_code=hotel_data['postal'],
            city=city,
            country=city.country,
            stars=hotel_data.get('stars', 3),
            hotel_video=f'hotel_videos/hotel_{i + 1}.mp4',
            description_en=hotel_data['desc_en'],
            description_ru=hotel_data['desc_ru'],
            owner=random.choice(owners)
        )

        # Добавляем случайные услуги (от 4 до 8)
        hotel_services = random.sample(services, random.randint(4, min(8, len(services))))
        hotel.service.set(hotel_services)

        hotels.append(hotel)

        # Создаем 4 изображения для каждого отеля
        for j in range(4):
            HotelImage.objects.create(
                hotel=hotel,
                hotel_image=f'hotel_images/hotel_{i + 1}_{j + 1}.png'
            )

    print(f"Создано {len(hotels)} отелей и {len(hotels) * 4} изображений")
    return hotels


def populate_rooms(hotels):
    """Создание номеров"""
    print("Создание номеров...")

    room_types = ['стандарт', 'семейный', 'одноместный', 'люкс']
    room_statuses = ['занят', 'забронирован', 'свободен']

    room_descriptions = {
        'стандарт': {
            'en': 'Comfortable standard room with modern amenities. Queen-size bed, work desk, flat-screen TV, mini-bar, and private bathroom with shower.',
            'ru': 'Комфортабельный стандартный номер с современными удобствами. Двуспальная кровать, рабочий стол, телевизор с плоским экраном, мини-бар и собственная ванная комната с душем.'
        },
        'семейный': {
            'en': 'Spacious family room with separate sleeping areas. Two double beds, sofa, kitchenette, dining table, and large bathroom. Perfect for families with children.',
            'ru': 'Просторный семейный номер с отдельными спальными зонами. Две двуспальные кровати, диван, мини-кухня, обеденный стол и большая ванная комната. Идеально для семей с детьми.'
        },
        'одноместный': {
            'en': 'Cozy single room ideal for solo travelers. Single bed, wardrobe, work area, free WiFi, and compact bathroom. Great value for business trips.',
            'ru': 'Уютный одноместный номер, идеальный для индивидуальных путешественников. Односпальная кровать, гардероб, рабочая зона, бесплатный WiFi и компактная ванная. Отличный вариант для командировок.'
        },
        'люкс': {
            'en': 'Luxurious suite with premium furnishings. King-size bed, separate living room, dining area, luxury bathroom with jacuzzi, city/ocean view, and VIP amenities.',
            'ru': 'Роскошный люкс с премиальной мебелью. Королевская кровать, отдельная гостиная, обеденная зона, роскошная ванная с джакузи, вид на город/океан и VIP-удобства.'
        }
    }

    base_prices = {
        'стандарт': Decimal('5000'),
        'одноместный': Decimal('3500'),
        'семейный': Decimal('8000'),
        'люкс': Decimal('15000')
    }

    rooms = []
    for hotel in hotels:
        # Создаем 10 номеров для каждого отеля
        for room_num in range(1, 11):
            room_type = random.choice(room_types)

            # Цена зависит от типа номера и звездности отеля
            stars = hotel.stars or 3
            price = (base_prices[room_type] * Decimal(str(stars))) / Decimal('3')

            room = Room.objects.create(
                hotel=hotel,
                room_number=100 + room_num,
                room_type=room_type,
                room_status=random.choice(room_statuses),
                price=price,
                description_en=room_descriptions[room_type]['en'],
                description_ru=room_descriptions[room_type]['ru']
            )
            rooms.append(room)

            # Создаем 3 изображения для каждого номера
            for j in range(3):
                RoomImage.objects.create(
                    room=room,
                    image=f'room_images/room_{room.id}_{j + 1}.png'
                )

    print(f"Создано {len(rooms)} номеров и {len(rooms) * 3} изображений")
    return rooms


def populate_bookings(clients, hotels, rooms):
    """Создание бронирований"""
    print("Создание бронирований...")

    bookings = []
    for i in range(10):
        client = random.choice(clients)
        room = random.choice(rooms)

        # Случайная дата заезда в пределах последних 60 дней или будущих 90 дней
        days_offset = random.randint(-60, 90)
        check_in = date.today() + timedelta(days=days_offset)

        # Длительность пребывания от 2 до 14 дней
        stay_duration = random.randint(2, 14)
        check_out = check_in + timedelta(days=stay_duration)

        booking = Booking.objects.create(
            user=client,
            hotel=room.hotel,
            room=room,
            check_in=check_in,
            check_out=check_out
        )
        bookings.append(booking)

    print(f"Создано {len(bookings)} бронирований")
    return bookings


def populate_reviews(clients, hotels):
    """Создание отзывов"""
    print("Создание отзывов...")

    reviews_data = [
        {
            'en': 'Excellent hotel! Amazing service, clean rooms, and friendly staff. The location is perfect and breakfast was delicious. Highly recommend!',
            'ru': 'Отличный отель! Потрясающий сервис, чистые номера и дружелюбный персонал. Расположение идеальное, а завтрак был вкусным. Очень рекомендую!'
        },
        # ... (добавь остальные элементы аналогично)
    ]

    reviews = []
    for i in range(min(10, len(reviews_data))):
        # Генерируем случайную дату в прошлом
        random_date = datetime.now() - timedelta(days=random.randint(1, 365))

        # Создаем отзыв с created_date
        review = Review.objects.create(
            user=random.choice(clients),
            hotel=random.choice(hotels),
            stars=random.randint(4, 5),
            text_en=reviews_data[i]['en'],
            text_ru=reviews_data[i]['ru'],
            created_date=random_date
        )
        reviews.append(review)

    print(f"Создано {len(reviews)} отзывов")
    return reviews


def main():
    """Главная функция"""
    print("=" * 80)
    print("НАЧАЛО ЗАПОЛНЕНИЯ БАЗЫ ДАННЫХ СИСТЕМЫ БРОНИРОВАНИЯ ОТЕЛЕЙ")
    print("=" * 80)

    # Очищаем базу данных
    clear_data()

    # Заполняем данные в правильном порядке
    countries = populate_countries()
    cities = populate_cities(countries)
    services = populate_services()
    clients, owners = populate_users(countries)
    hotels = populate_hotels(cities, services, owners)
    rooms = populate_rooms(hotels)
    bookings = populate_bookings(clients, hotels, rooms)
    reviews = populate_reviews(clients, hotels)

    print("=" * 80)
    print("БАЗА ДАННЫХ УСПЕШНО ЗАПОЛНЕНА!")
    print("=" * 80)
    print(f"Всего создано:")
    print(f"  - Стран: {len(countries)}")
    print(f"  - Городов: {len(cities)}")
    print(f"  - Услуг: {len(services)}")
    print(f"  - Клиентов: {len(clients)}")
    print(f"  - Владельцев отелей: {len(owners)}")
    print(f"  - Отелей: {len(hotels)}")
    print(f"  - Изображений отелей: {len(hotels) * 4}")
    print(f"  - Номеров: {len(rooms)}")
    print(f"  - Изображений номеров: {len(rooms) * 3}")
    print(f"  - Бронирований: {len(bookings)}")
    print(f"  - Отзывов: {len(reviews)}")
    print(f"\nВсе данные на двух языках: English, Русский")
    print("=" * 80)


if __name__ == '__main__':
    main()
