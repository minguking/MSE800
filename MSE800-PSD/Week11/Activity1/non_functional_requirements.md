# Non-Functional Requirements — WeatherWear+

| ID | Requirement | Category | Priority | Status |
|----|-------------|----------|----------|--------|
| NFR-01 | Standard API endpoints respond within 2 seconds under normal load | Performance | Must Have |    |
| NFR-02 | Dashboard page fully loads within 3 seconds on a standard connection | Performance | Must Have |    |
| NFR-03 | AI recommendation responses complete within 10 seconds; loading spinner shown during wait | Performance | Must Have |    |
| NFR-04 | Passwords stored using bcrypt hashing — no plaintext in the database | Security | Must Have |    |
| NFR-05 | All API secrets and keys managed via environment variables and never committed to Git | Security | Must Have |    |
| NFR-06 | All input validated through Pydantic schemas; SQLAlchemy ORM used (no raw SQL) | Security | Must Have |    |
| NFR-07 | Production deployment served over HTTPS; HTTP redirected automatically | Security | Must Have |    |
| NFR-08 | All error responses return structured JSON — no raw stack traces exposed to users | Reliability | Must Have |    |
| NFR-09 | Application handles weather API and AI API failures gracefully with user-friendly messages | Reliability | Must Have |    |
| NFR-10 | Application is fully functional on screens as small as 375px wide (mobile-first) | Usability | Must Have |    |
| NFR-11 | Loading indicators appear during all async operations — no blank screens | Usability | Must Have |    |
| NFR-12 | Dark mode toggle available in the navbar; preference saved in localStorage | Usability | Could Have |    |
| NFR-13 | Backend test suite achieves minimum 80% code coverage (achieved: 82%) | Maintainability | Must Have |    |
| NFR-14 | GitHub Actions CI pipeline runs full test suite on every push and pull request | Maintainability | Must Have |    |
| NFR-15 | All FastAPI endpoints are stateless — authentication handled entirely via JWT | Scalability | Must Have |    |
