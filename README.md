# BotFarm Microservice

## Description
This project is a RESTful microservice designed to emulate real user interactions for E2E testing in web applications. It uses FastAPI for the web framework and SQLAlchemy as the ORM, ensuring a high-performance backend suitable for detailed testing scenarios.

## Features
- User Management: Create and manage user entities with secure password storage.
- User Locking Mechanism: Acquire and release locks on users to simulate concurrent accesses, vital for E2E testing scenarios.
- RESTful API: The API provides endpoints to create users, list users, acquire locks, and release locks, facilitating integration with test suites.

## Technologies
- FastAPI & Uvicorn: For a high-performance, asynchronous API server.
- SQLAlchemy (v2): For robust database management.
- PostgreSQL (v14+): Chosen for its advanced features and reliability.
- Pydantic (v1 or v2): For data validation and settings management.
- pytest: For comprehensive testing, aiming for at least 75% coverage.

## System Requirements
- PostgreSQL 14 or higher
- Python 3.8 or higher

## Setup & Installation
1. Clone the repository.
2. Set up a PostgreSQL database.
3. Install dependencies using pip install -r requirements.txt.
4. Configure environment variables for database access.
5. Run the application with uvicorn main:app --reload.

## Testing
Utilize pytest for running unit tests. Ensure that your tests cover at least 75% of the codebase.

## Deployment
- Docker: The service is containerized with Docker, deployable using Docker Compose.
- Kubernetes: Prepared for deployment on Kubernetes platforms like Minikube.

## Additional Features
- Asynchronous Support: Complete async support with asyncio and asyncpg.
- Database Migrations: Managed with Alembic for straightforward database schema updates.
- Authentication: Optional OAuth2 authentication for enhanced security.

## Contributing
Contributions to the project are welcome! Please ensure that your contributions adhere to the project's coding style, including function naming, doc-strings, and type-hints.

## License
This project is licensed under the terms of the MIT license.
