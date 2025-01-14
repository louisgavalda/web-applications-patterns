# Web Applications Patterns
  Web Applications Patterns course @ [EPITA](https://www.epita.fr/) / January 2025
  with [Louis Gavalda](https://www.linkedin.com/in/louis-gavalda/).

# About this course

## Objectives

- __Discuss and learn__ about a few of the most __common patterns__ used in web applications.
- __Build__ something together -- and by doing so, learn to apply them in your own projects.
- Have fun.

And more precisely, we are going to build:
- a **Django** web application for... 🥁 books management.
- a **REST API** (using Django Ninja) on top of our Django application.
- a basic **SPA** (using Svelte) for consuming content from our API.

## Prerequisites

- Be curious.
- Be confident in your thinking/coding ability.
- Be confortable using a terminal.
- Know how to read (documentation).

## Where to begin

Download or clone this repository:
https://github.com/louisgavalda/web-applications-patterns

```bash
git clone https://github.com/louisgavalda/web-applications-patterns.git web-applications-patterns-git
```

Execute these commands in your terminal in order to install and run the Django app:
```bash
# Change directory, we go into to the project folder
cd web-applications-patterns-git
# Create a new Python virtual environment named 'venv'
python3 -m venv venv
# Activate the virtual environment
source ./venv/bin/activate
# Install all project dependencies listed in requirements.txt
pip install -r requirements.txt
# Generate database migration files (based on model changes)
./manage.py makemigrations
# Create an admin user account with the specified (dummy) email
./manage.py createsuperuser --email user@example.com
# Start the Django development server in debug mode
DEBUG=1 ./manage.py runserver
```

Open your browser and go to http://127.0.0.1:8000/

If everything is OK, you should see this message:
```text
yes, it works! 👍
```

# A few commonly used patterns

## Model-View-Controller (MVC)

### What?

The MVC (Model-View-Controller) pattern is a fundamental **architectural pattern** that divides a web application into **three** distinct but interconnected components:

#### (1) Model
*The brain and data manager*

The **Model** represents your application's data structure and business logic.

- Manages data, business rules, logic, and operations
- Interacts with your database
- Maintains the integrity of your data
- Is completely independent of the user interface

**Example**: In a blog application, the **Model** would handle:
- Post creation and validation
- User authentication rules
- Comment management
- Database interactions

#### (2) View
*The face of your application*

The **View** is responsible for presenting data to users.

- Renders the user interface
- Displays data in a human-readable format
- Handles the visual presentation logic
- Receives data from the **Controller**

**Example**: In a blog application, Views would include:
- The homepage template showing recent posts
- The user profile page layout
- The comment submission form
- The admin dashboard interface

#### (3) Controller
*The traffic director*

The **Controller** mediates between the Model and View.

- Processes incoming requests from users
- Coordinates between **Model** and **View**
- Makes decisions about which data to fetch
- Determines which **View** to display

**Example**: When a user creates a new blog post:
1. The Controller receives the form submission
2. Validates the input data
3. Tells the Model to create a new post
4. Chooses the appropriate View to display (success or error page)

#### Flow of Information

![from [Wikipédia](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller)](img/MVC-Process.svg.png)

1. User interacts with the View (clicks a button, submits a form)
2. Controller receives the request
3. Controller processes the request and interacts with the Model if needed
4. Model performs business logic and data operations
5. Controller receives results from the Model
6. Controller selects and updates the appropriate View
7. Updated View is presented to the user

This separation of concerns leads to:
- More maintainable code
- Easier debugging
- Better code organization
- Simpler testing
- Enhanced scalability

### Why?

_To be discussed during the course._

### How?

Example with the Python [Django](https://www.djangoproject.com/) framework which is built around a MVC (or [MTV](https://docs.djangoproject.com/en/5.1/faq/general/#django-appears-to-be-a-mvc-framework-but-you-call-the-controller-the-view-and-the-view-the-template-how-come-you-don-t-use-the-standard-names)?) pattern.

We will draw inspiration from the famous [Django tutorial](https://docs.djangoproject.com/en/5.1/intro/tutorial01/).
Read the first part of the tutorial, and maybe the beginning of the [second one](https://docs.djangoproject.com/en/5.1/intro/tutorial02/) if you're curious.

We will create an app for... 🥁 books management.

### See also

- http://wiki.c2.com/?ModelViewController=

## RESTful Services

### What?

_To be discussed during the course._

### Why?

_To be discussed during the course._

### How?

We will use [Django Ninja](https://django-ninja.dev/) to add a REST to our Django application.

See the [Django Ninja tutorial](https://django-ninja.dev/tutorial/).
Django Ninja is already installed, you don't need to take care of that.
Simply draw inspiration from the [CRUD example](https://django-ninja.dev/tutorial/other/crud/) and try to adapt it for our books management application.

## Single Page Application (SPA)

### What?
### Why?
### How?

## Observer Pattern

### What?
### Why?
### How?
### See also

- [Observer pattern](https://refactoring.guru/design-patterns/observer)

## Microservices

### What?
### Why?
### How?

## Extra reading

- [Catalog of Patterns of Enterprise Application Architecture](https://martinfowler.com/eaaCatalog/index.html)
- [Anti-pattern](https://en.wikipedia.org/wiki/Anti-pattern)
