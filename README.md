# BookingProjectss

An educational hotel-booking backend built with **Django REST Framework**.

The project includes hotel and room listings, booking and review
operations, JWT authentication, filtering and pagination.

## Features

- User registration, login and logout
- JWT authentication with SimpleJWT
- City, hotel and room endpoints
- Hotel and room filtering, search and ordering
- Pagination for listing endpoints
- Booking and review operations
- User-scoped booking and review querysets
- Custom permission classes referenced in the implementation

Features are described from source code.
Their presence does not guarantee that every scenario has been tested.

## Technology Stack

| Area | Technologies |
| :--- | :--- |
| Language | Python |
| Framework | Django |
| API | Django REST Framework |
| Authentication | SimpleJWT |
| Filtering | django-filter |
| Deployment configuration | Docker, Docker Compose, nginx |

A SQLite database file is included in the repository.
Use a fresh development database and sanitized sample data.

## Project Structure

```text
BookingProjectss/
└── mysite/
    ├── manage.py
    ├── booking_app/         # Application and API logic
    ├── nginx/               # Reverse proxy configuration
    ├── Dockerfile
    ├── docker-compose.yml
    └── req.txt              # Python dependencies
```

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/minbaevv/BookingProjectss.git
cd BookingProjectss
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

Activate it on Linux/macOS:

```bash
source .venv/bin/activate
```

Or on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
cd mysite
python -m pip install -r req.txt
```

### 4. Configure the environment

Review the Django settings and configure the required local
environment variables before startup.

Use a newly generated local secret key. Do not publish working
credentials, private uploads or real user data.

### 5. Apply migrations and start the server

```bash
python manage.py migrate
python manage.py runserver
```

Default development address:

```text
http://127.0.0.1:8000/
```

Check the project's URL configuration for the available API paths.
An API-only application does not require a frontend homepage.

These setup instructions are source-derived and still require
verification in a clean environment.

## Known Issue

In the reviewed implementation, `HotelViewSet` uses
`permissions_classes` instead of DRF's `permission_classes`.

The intended class-level permission policy is not applied through
that misspelled attribute. Correct it and test unauthorized requests.

Global permission defaults must also be checked; the typo alone
does not prove that every endpoint is publicly writable.

## Booking and Authorization Checks

Before deployment, verify that:

- Protected actions require authentication
- Hotel and room changes enforce the intended ownership rules
- Users cannot modify another user's bookings or reviews
- Check-in and check-out dates are valid
- Availability rules prevent conflicting reservations
- Concurrent booking requests are handled correctly
- Filtering, search and ordering use valid model fields

## Development Priorities

- Correct the permission attribute in `HotelViewSet`
- Review model/serializer imports and replace wildcard imports
- Document environment variables in a safe `.env.example`
- Remove private configuration and real database contents from Git
- Add or extend authentication and ownership tests
- Test booking overlap and concurrent reservation behavior
- Add request and response examples
- Verify Docker startup in a clean environment
- Configure continuous integration

## Project Status

This repository demonstrates backend development practice.
It is not presented as a production-ready booking service.

Runtime behavior, permissions, availability rules and deployment
configuration require further validation.

## Attribution and License

Retain attribution for any course, tutorial or external code used.
Document your own additions and changes.

Check the repository's licensing and rights to media before reuse.

## Author

**Kubanychbek Duishekeev**

[GitHub](https://github.com/minbaevv) ·
[LinkedIn](https://www.linkedin.com/in/kubanychbek-duishekeev-7b9872427/) ·
[Telegram](https://t.me/d_kubanychbek) ·
[Gmail](mailto:duishekeevkubanychbek@gmail.com)
