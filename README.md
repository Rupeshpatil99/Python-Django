# Django Project: Dproject & GOT

A Django project for learning and practicing Django fundamentals,
including project organization, URL routing, views, HTML templates,
static files, and the request-response cycle.

## Project Structure

The structure below combines the project and GOT app folders shown in
the VS Code screenshots.

``` text
Dproject/
│
├── Dproject/                         # Main Django project package
│   ├── templates/
│   │   └── website/
│   │       └── index.html            # Main website template
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py                   # Project configuration
│   ├── urls.py                       # Main URL configuration
│   └── views.py                      # Project-level views
│
├── GOT/                              # GOT Django application
│   ├── migrations/                   # Database migrations
│   ├── templates/
│   │   └── GOT/
│   │       └── all_got.html          # GOT app template
│   ├── __pycache__/                  # Python-generated cache (not committed)
│   ├── __init__.py
│   ├── admin.py                      # Django admin configuration
│   ├── apps.py                       # App configuration
│   ├── models.py                     # Data models
│   ├── tests.py                      # Tests
│   ├── urls.py                       # App URL routes
│   └── views.py                      # App view functions
│
├── static/
│   └── style.css                     # CSS styles
│
├── db.sqlite3                        # SQLite database (local development)
└── manage.py                         # Django command-line utility
```

> `__pycache__` and usually `db.sqlite3` are local/generated files.
> Consider excluding them from Git unless you have a specific reason to
> track the database.

## Project Overview

The project is organized into:

-   **`Dproject/`**: Main Django configuration package, including
    settings and the root URL configuration.
-   **`GOT/`**: A Django app containing its own views, URL patterns,
    templates, models, and tests.
-   **`templates/`**: HTML files rendered by Django.
-   **`static/`**: Frontend assets such as CSS.
-   **`db.sqlite3`**: SQLite database used for local development.
-   **`manage.py`**: Utility for running the development server and
    other Django management commands.

## Request-Response Flow

For a request to the GOT page, the flow is typically:

``` text
Browser
   |
   | GET /GOT/
   v
Dproject/urls.py
   |
   | includes GOT.urls
   v
GOT/urls.py
   |
   | matches route
   v
GOT/views.py
   |
   | renders GOT/all_got.html
   v
Browser displays the page
```

The actual route behavior depends on the URL patterns and view code in
your project.

## URL Configuration

A typical main URL configuration in `Dproject/urls.py` can include the
GOT app like this:

``` python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("GOT/", include("GOT.urls")),
]
```

The app-level `GOT/urls.py` can define its route like this:

``` python
from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_got, name="all_got"),
]
```

This maps `/GOT/` to the `all_got` view, assuming that function is
defined in `GOT/views.py`.

## Templates and Static Files

  File                                      Purpose
  ----------------------------------------- -------------------
  `Dproject/templates/website/index.html`   Main website page
  `GOT/templates/GOT/all_got.html`          GOT app page
  `static/style.css`                        Stylesheet

Django templates allow views to return dynamic HTML. Static files such
as CSS are used to style the pages.

For project-level templates, check the `TEMPLATES` configuration in
`Dproject/settings.py`. For static files, configure `STATIC_URL` and any
needed static directories in settings.

## Run Locally

Run these commands from the directory containing `manage.py`.

### 1. Create and activate a virtual environment

**Windows PowerShell:**

``` powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2. Install Django

``` powershell
python -m pip install django
```

If your repository has a `requirements.txt` file, install dependencies
with:

``` powershell
python -m pip install -r requirements.txt
```

### 3. Apply database migrations

``` powershell
python manage.py migrate
```

### 4. Start the development server

``` powershell
python manage.py runserver
```

Open `http://127.0.0.1:8000/` and navigate to the routes configured in
your URL files. If the GOT route is configured as shown above, visit:

`http://127.0.0.1:8000/GOT/`

## Common Django Concepts Practiced

-   **Project and app structure:** Separating site configuration from
    app-specific functionality.
-   **URL dispatcher:** Mapping paths to view functions.
-   **Views:** Processing requests and returning responses.
-   **Templates:** Rendering HTML pages.
-   **Static files:** Serving CSS and other frontend assets during
    development.
-   **Models and migrations:** Defining data and tracking database
    schema changes.
-   **Testing:** Writing checks for application behavior.

## Troubleshooting

### ImportError: cannot import name `GOT` from `Dproject`

Avoid using `from Dproject import GOT` to connect the app unless you
explicitly created that name in the package.

Use `include()` in the main URL configuration:

``` python
from django.urls import path, include

urlpatterns = [
    path("GOT/", include("GOT.urls")),
]
```

Inside `GOT/urls.py`, use a local views import:

``` python
from . import views
```

Also confirm that `GOT/urls.py` defines `urlpatterns`, that
`GOT/views.py` contains the referenced view, and that `GOT` is listed in
`INSTALLED_APPS` in `settings.py`.

### TemplateDoesNotExist

Check the spelling and capitalization of the template path. For example,
if the view renders `GOT/all_got.html`, the file should be located at:

`GOT/templates/GOT/all_got.html`

### Static CSS not loading

Check `STATIC_URL` and ensure the template references static assets
using Django's static template tag. During development, confirm
`django.contrib.staticfiles` is enabled.

## Suggested `.gitignore`

``` gitignore
.venv/
__pycache__/
*.py[cod]
db.sqlite3
.env
```

If you intentionally need to share a development database, remove
`db.sqlite3` from `.gitignore` and consider whether it contains data
that should be public.

## Future Improvements

-   Document each page and route as the project grows.
-   Add screenshots of the running website.
-   Add tests for URL patterns and views.
-   Add `requirements.txt` to record dependencies.
-   Expand the app with database-backed features if needed.

## License

No license is specified yet. Add a license file if you plan to publish
the project for reuse.

