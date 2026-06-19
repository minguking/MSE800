# Functional Requirements — WeatherWear+

| ID | Requirement | Priority | Status |
|----|-------------|----------|--------|
| FR-01 | Users can register with a unique email, username, and password (min. 8 characters) | Must Have |  |
| FR-02 | Passwords are stored as bcrypt hashes — no plaintext ever saved | Must Have |  |
| FR-03 | Registered users can log in with email and password and receive a JWT token | Must Have |  |
| FR-04 | All protected endpoints reject requests with missing or invalid JWT tokens | Must Have |  |
| FR-05 | Users can log out by clearing their token on the client side | Must Have |  |
| FR-06 | Users can view and update their profile (username, location, bio, avatar) | Should Have |   |
| FR-07 | The app fetches real-time weather data for any city via the Open-Meteo API | Must Have |   |
| FR-08 | Weather response includes temperature, feels-like, humidity, wind speed, description, and icon | Must Have |   |
| FR-09 | Weather data for the same user/city/day is cached in the database to avoid repeated API calls | Should Have |   |
| FR-10 | Users can log an outfit (description, date, rating 1–5, notes) | Must Have |   |
| FR-11 | Users can view, edit, and delete their past outfit logs | Should Have |   |
| FR-12 | Outfit history supports pagination and date range filtering | Should Have |   |
| FR-13 | The app generates an AI outfit recommendation using current weather and the user's recent outfit history | Must Have |   |
| FR-14 | Users can view the outfit they wore on the same date one year ago | Should Have |   |
| FR-15 | Users can chat with an AI assistant that maintains conversation history within a session | Should Have |   |
