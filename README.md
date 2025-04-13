# Base-Repo
This is a python projects base repository


Project structure
```
istandard/
│
├── alembic/
│   ├── versions/              # Migration scripts will go here
│   └── alembic.ini            # Alembic configuration file
│
├── app/
│   ├── __init__.py            # Initialize the app module
│   ├── main.py                # Entry point for FastAPI (starts the app)
│   ├── config/                # Configuration folder
│   │   └── settings.py        # Settings file (database URL, etc.)
│   ├── accounts/              # Accounts feature (user registration, login, etc.)
│   │   ├── __init__.py
│   │   ├── models/            # Database models for accounts
│   │   │   ├── __init__.py
│   │   │   └── user.py        # User model
│   │   ├── schemas/           # Pydantic schemas for accounts
│   │   │   ├── __init__.py
│   │   │   └── user.py        # User schema (for request/response validation)
│   │   ├── routes/            # Routes for accounts (user-related tasks)
│   │   │   ├── __init__.py
│   │   │   └── user.py        # User routes (registration, login)
│   │   └── db.py              # Database connection for accounts
│   ├── products/              # Products feature (can follow the same pattern)
│   │   ├── __init__.py
│   │   ├── models/            # Database models for products
│   │   │   ├── __init__.py
│   │   │   └── product.py     # Product model
│   │   ├── schemas/           # Pydantic schemas for products
│   │   │   ├── __init__.py
│   │   │   └── product.py     # Product schema
│   │   ├── routes/            # Routes for products
│   │   │   ├── __init__.py
│   │   │   └── product.py     # Product routes
│   │   └── db.py              # Database connection for products
│
├── requirements.txt           # Project dependencies
├── alembic.ini                # Alembic settings
└── README.md                  # Project documentation
```

# How to run the project

```bash
pip install -r requirements.txt
alembic upgrade head
uvicorn app.main:app --reload
```

<hr>
<hr>

### Alembic Commands
Here are the commands you will use for managing migrations in your project:

Create a Migration File (equivalent to Django's makemigrations): After making changes to your models (e.g., adding a new field to your user model), run this command to generate the migration file:
```bash
alembic revision --autogenerate -m "Add created_at field to User model"
```

This command will generate a migration script in the alembic/versions/ directory with the given message ("Add created_at field to User model").

The migration file will contain the changes to your database schema (e.g., adding or altering tables, columns, etc.).

Apply the Migrations (equivalent to Django's migrate): To apply the migrations and update the database, run this command:

```bash
alembic upgrade head
```
This will apply the migrations to the most recent revision (head), ensuring that the database schema is up to date.

<hr>

### Example Downgrade Commands:
Downgrade all migrations (rollback to the initial state):

```bash
alembic downgrade base
```
Downgrade to a specific revision (e.g., revision ID 1234567890ab):
```bash
alembic downgrade 1234567890ab
```

Downgrade one step back:
```bash
alembic downgrade -1
```
<hr>
<hr>