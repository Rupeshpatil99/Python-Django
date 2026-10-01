# Django Project – Dproject & GOT

A beginner-friendly Django project to practice backend development, URL routing, HTML templates, static files, and MySQL database integration.

## Technologies Used

* Python
* Django
* MySQL
* HTML
* CSS
* Git & GitHub

## Project Structure

```text
Dproject/
│
├── Dproject/
│   ├── settings.py
│   ├── urls.py
│   └── views.py
│
├── GOT/
│   ├── migrations/
│   ├── templates/
│   │   └── GOT/
│   │       └── all_got.html
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
├── static/
│   └── style.css
│
├── manage.py
└── requirements.txt
```

## Features

* Django project and app structure
* URL routing and views
* HTML templates
* CSS styling
* MySQL database connection
* Django ORM and migrations

## Database

This project uses **MySQL** for database management.

Create the database:

```sql
CREATE DATABASE got_db;
```

Configure MySQL in `Dproject/settings.py`:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "got_db",
        "USER": "your_username",
        "PASSWORD": "your_password",
        "HOST": "localhost",
        "PORT": "3306",
    }
}
```

## Installation & Run

**1. Clone the repository**

```bash
git clone <your-repository-url>
cd Dproject
```

**2. Create and activate virtual environment**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

If you don't have a requirements file yet:

```bash
pip install django mysqlclient
```

**4. Apply migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

**5. Run the server**

```bash
python manage.py runserver
```

Open: `http://127.0.0.1:8000/`

GOT page: `http://127.0.0.1:8000/GOT/` (if configured)

## Learning Goals

* Understand Django project structure
* Practice URL patterns and views
* Render dynamic HTML using templates
* Connect Django with MySQL
* Learn database operations using Django ORM

## Future Improvements

* [ ] Add CRUD operations
* [ ] Improve frontend design
* [ ] Add form validation
* [ ] Add user authentication
* [ ] Write Django tests

## Author

**Rupesh Patil**

Django Backend Development Practice Project
