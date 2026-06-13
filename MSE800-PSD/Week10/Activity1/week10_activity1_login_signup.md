# Week 10 - Activity 1: Login & Signup System

This document covers the Login and Signup system implemented for **WeatherWear+**, an AI-powered outfit recommendation web application. The authentication system is built as a full-stack solution using a FastAPI backend and a React frontend, with JWT-based session management and bcrypt password hashing.

---

## Core Features

- User signup (registration)
- User login
- Personal profile management:
  - Username
  - Email
  - Default city (location)
  - Avatar colour and URL
  - Bio
- JWT-based session persistence
- Logout
- Password hashing for secure storage

---

## Functional Design Overview

### Backend (`backend/app/`)

- **`routes/users.py`**
  Defines all authentication API endpoints under `/api/v1/users`.

- **`POST /register`**
  Collects username, email, password, and optional location. Validates uniqueness of email and username, hashes the password, creates the user record, and returns a JWT token alongside the user profile.

- **`POST /login`**
  Accepts email and password. Verifies the password against the stored bcrypt hash and returns a JWT token on success.

- **`GET /me`**
  Returns the currently authenticated user's profile. Requires a valid Bearer token.

- **`PUT /me`**
  Allows the authenticated user to update their username, location, avatar, and bio.

- **`utils/auth.py`**
  A shared security module used across the entire auth flow:
  - `hash_password` — bcrypt-hashes a plain-text password before storage.
  - `verify_password` — compares a plain-text input with the stored hash at login.
  - `create_access_token` — generates a signed HS256 JWT with an expiry.
  - `get_current_user` — FastAPI dependency that decodes the Bearer token and retrieves the user from the database on every protected request.

- **`models/user.py`**
  SQLAlchemy ORM model defining the `users` table with fields: `id`, `username`, `email`, `password_hash`, `location`, `avatar_color`, `avatar_url`, `bio`, `created_at`.

- **`schemas/user.py`**
  Pydantic schemas for request validation and response serialisation:
  - `UserCreate` — validates username format (3–50 chars, alphanumeric), email format, and minimum password length (8 chars).
  - `UserLogin` — email and password pair.
  - `UserResponse` — safe public profile (excludes password hash).
  - `UserUpdate` — partial update fields.
  - `TokenResponse` — wraps the access token and user profile returned after login/register.

### Frontend (`frontend/src/`)

- **`pages/Login.jsx`**
  Renders the login form (email + password). On submit, calls `authApi.login()`, stores the returned token via `AuthContext`, and redirects to the dashboard.

- **`pages/Register.jsx`**
  Renders the signup form (username, email, password, optional city). On submit, calls `authApi.register()`, stores the token via `AuthContext`, and redirects to the dashboard.

- **`context/AuthContext.jsx`**
  Global React context that manages authentication state across the app:
  - `login(token, user)` — persists token and user to `localStorage` and updates state.
  - `logout()` — clears `localStorage` and resets state.
  - `isAuthenticated` — boolean derived from token presence, used by route guards.

- **`services/api.js`**
  Axios instance with base URL configuration. `authApi.login()` and `authApi.register()` are the two auth-specific methods that post to the backend endpoints.

---

## Design Diagram Summary

The function design below shows how the Login & Signup system is structured across the full stack:

```
Login & Signup System
├── Register Flow
│   ├── Register Page (React)
│   │   ├── Collect username, email, password, city
│   │   └── Call POST /api/v1/users/register
│   └── Register Endpoint (FastAPI)
│       ├── Validate input (UserCreate schema)
│       ├── Check email & username uniqueness
│       ├── Hash Password (bcrypt)
│       ├── Save User to DB
│       └── Return JWT Token + User Profile
│
├── Login Flow
│   ├── Login Page (React)
│   │   ├── Collect email and password
│   │   └── Call POST /api/v1/users/login
│   └── Login Endpoint (FastAPI)
│       ├── Look up user by email
│       ├── Verify Password (bcrypt compare)
│       └── Return JWT Token + User Profile
│
├── Session Management (AuthContext)
│   ├── Store JWT in localStorage
│   ├── Expose user & isAuthenticated to all pages
│   └── Clear on logout
│
└── Protected Routes
    ├── GET /me — decode token → load user
    └── PUT /me — update profile fields
```

---

## Example User Flow

1. A new user opens the app and clicks **Sign Up**.
2. They enter a username, email, password (min. 8 characters), and optionally a default city.
3. The frontend sends a `POST /api/v1/users/register` request.
4. The backend validates the input, hashes the password with bcrypt, and saves the user.
5. A signed JWT is returned and stored in `localStorage` by `AuthContext`.
6. The user is redirected to the Dashboard as an authenticated session.
7. On return visits, the stored token is read from `localStorage` on app load — the user stays logged in.
8. When the user logs in with an existing account, the backend compares the entered password against the stored hash via `verify_password`.
9. On logout, the token and user data are cleared from `localStorage` and the user is returned to the Login page.

---

## Tech Stack

| Layer     | Technology                              |
|-----------|-----------------------------------------|
| Frontend  | React 18, React Router v6, Axios        |
| Backend   | FastAPI, SQLAlchemy 2, Pydantic v2      |
| Auth      | JWT (python-jose HS256), bcrypt 4       |
| Database  | SQLite (via SQLAlchemy ORM)             |

---

## Run the System

### Backend

1. Create and activate a virtual environment:
   ```bash
   cd backend
   python -m venv .venv && source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy the environment file and set required values:
   ```bash
   cp .env.example .env
   ```
4. Start the API server:
   ```bash
   uvicorn app.main:app --reload
   ```
5. The API will be available at `http://localhost:8000`.

### Frontend

1. Install dependencies:
   ```bash
   cd frontend
   npm install
   ```
2. Start the development server:
   ```bash
   npm run dev
   ```
3. Open `http://localhost:5173` in your browser and navigate to `/register` or `/login`.
