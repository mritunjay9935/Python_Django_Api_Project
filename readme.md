```markdown
# My Django Project

This is a Django project with a single app called `myapp`. The project uses Django REST Framework to create a simple API for managing `User` objects.

## Project Structure

The project has the following structure:

```
myproject/
    manage.py
    myproject/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
    myapp/
        migrations/
            __init__.py
        __init__.py
        admin.py
        apps.py
        models.py
        tests.py
        views.py
        serializers.py
```

## Installation

1. Clone the repository and navigate into the project directory:

```bash
git clone <repository_url>
cd <repository_name>
```

2. Make sure you have Django and Django REST Framework installed. If not, you can install them using pip:

```bash
pip install django djangorestframework
```

3. Run migrations to create the database schema:

```bash
python manage.py migrate
```

## Running the Server

You can start the Django development server using the following command:

```bash
python manage.py runserver
```

By default, the server runs on port 8000. If you want to change the port, you can specify it as a command line argument:

```bash
python manage.py runserver 8080
```

## API Endpoints

The project includes the following API endpoints:

- `GET /api/users`: List all users. Supports query parameters for pagination (`page`, `limit`), filtering by name (`name`), and sorting (`sort`).
- `POST /api/users`: Create a new user.
- `GET /api/users/<id>`: Retrieve the user with the given ID.
- `PUT /api/users/<id>`: Update the user with the given ID.
- `DELETE /api/users/<id>`: Delete the user with the given ID.

## Models

The `User` model is defined in `myapp/models.py` and includes the following fields:

- `first_name`: A character field with a maximum length of 100.
- `last_name`: A character field with a maximum length of 100.
- `company_name`: A character field with a maximum length of 100.
- `city`: A character field with a maximum length of 100.
- `state`: A character field with a maximum length of 100.
- `zip`: An integer field.
- `email`: An email field.
- `web`: A URL field.
- `age`: An integer field.

## Serializers

The `UserSerializer` is defined in `myapp/serializers.py` and is used to convert `User` instances to JSON and vice versa.

## Views

The views for the API endpoints are defined in `myapp/views.py` and use Django REST Framework's class-based views:

- `UserListCreate`: A view that handles `GET` and `POST` requests for `/api/users`.
- `UserRetrieveUpdateDestroy`: A view that handles `GET`, `PUT`, and `DELETE` requests for `/api/users/<id>`.

