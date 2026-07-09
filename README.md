# AI Grammar Checker API

A Django REST Framework backend that uses **Google Gemini AI** to detect and correct grammatical errors in text. Features JWT authentication, user-specific history, and structured AI responses.

## Tech Stack

- **Django 5.2** + **Django REST Framework**
- **Google Gemini 2.5 Flash** for grammar analysis
- **SimpleJWT** for token-based authentication
- **SQLite** (default, swap for PostgreSQL in production)

## Setup

### 1. Clone & Install

```bash
git clone https://github.com/adarsh-pathak-2006/AI-Grammer-Checker.git
cd AI-Grammer-Checker/grammer_checker
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux
pip install -r requirements.txt
```

### 2. Configure Environment

```bash
cp .env.example .env
```

Edit `.env` and fill in your values:

| Variable | Description |
|----------|-------------|
| `SECRET_KEY` | Django secret key (generate one for production) |
| `DEBUG` | `True` for development, `False` for production |
| `ALLOWED_HOSTS` | Comma-separated list of allowed hosts |
| `GEMINI_API_KEY` | Your Google Gemini API key |
| `CORS_ALLOWED_ORIGINS` | Comma-separated frontend origins |

### 3. Run Migrations & Start Server

```bash
python manage.py migrate
python manage.py createsuperuser  # optional
python manage.py runserver
```

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/register/` | Create a new user account |
| `POST` | `/token/` | Get JWT access + refresh tokens |
| `POST` | `/token/refresh/` | Refresh an expired access token |

### Grammar Checker (Requires JWT)

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/dashboard/` | List all your grammar check history |
| `POST` | `/dashboard/` | Submit text for grammar checking |
| `GET` | `/dashboard/<id>/` | Get a specific grammar check result |

### Request/Response Examples

**Register:**
```json
POST /register/
{
    "first_name": "John",
    "last_name": "Doe",
    "username": "johndoe",
    "email": "john@example.com",
    "password": "securepassword123"
}
```

**Get Token:**
```json
POST /token/
{
    "username": "johndoe",
    "password": "securepassword123"
}
// Returns: { "access": "...", "refresh": "..." }
```

**Check Grammar (with Bearer token):**
```json
POST /dashboard/
Authorization: Bearer <access_token>
{
    "input": "He go to the store yesterday and buyed some milk."
}
// Returns: { "corrected_text": "...", "mistakes": [...], "explanation": [...] }
```

## Project Structure

```
grammer_checker/
├── grammer_checker/        # Django project config
│   ├── settings.py         # Configuration (env-based)
│   ├── urls.py             # URL routing
│   ├── views.py            # API views
│   ├── models.py           # Database models
│   ├── serializers.py      # DRF serializers
│   └── admin.py            # Admin registration
├── services/               # AI integration layer
│   ├── ai_integration.py   # Gemini client
│   ├── build_prompt.py     # Prompt engineering
│   └── response.py         # Response parsing
├── .env.example            # Environment template
├── requirements.txt        # Python dependencies
└── manage.py               # Django CLI
```

## License

MIT
