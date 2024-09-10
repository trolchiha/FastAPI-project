# FastAPI Project

A simple FastAPI application with basic CRUD operations and authentication.

## Features

- User authentication and authorization
- Basic CRUD operations for managing posts
- Docker support for easy deployment

## Prerequisites

- Python 3.7+
- Docker (optional, for containerized deployment)

## Installation

### Using Docker

1. Clone the repository:

    ```bash
    git clone https://github.com/trolchiha/FastAPI-project.git
    cd FastAPI-project
    ```

2. Build and run the Docker containers:

    ```bash
    docker-compose up --build
    ```

### Without Docker

1. Clone the repository:

    ```bash
    git clone https://github.com/trolchiha/FastAPI-project.git
    cd FastAPI-project
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:

    ```bash
    uvicorn app.main:app --reload
    ```

## Configuration

Update the environment variables in the `.env` file or Docker environment configuration as needed.

## Usage

- Access the API at `http://localhost:8000`

## API Endpoints

- **POST /users**: Create a new user
- **GET /users/{user_id}**: Retrieve a user by ID
- **POST /login**: Authenticate a user and receive a JWT token
- **GET /posts**: Retrieve all posts
- **POST /posts**: Create a new post
- **GET /posts/{post_id}**: Retrieve a post by ID
- **PUT /posts/{post_id}**: Update a post by ID
- **DELETE /posts/{post_id}**: Delete a post by ID

## Testing

Run the tests using:

```bash
pytest
