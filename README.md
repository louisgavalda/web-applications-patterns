# Web Applications Patterns
  Web Applications Patterns course @ [EPITA](https://www.epita.fr/) / January 2025
  with [Louis Gavalda](https://www.linkedin.com/in/louis-gavalda/).

# About this course

## Objectives

- __Discuss and learn__ about a few of the most __common patterns__ used in web applications.
- __Build__ something together -- and by doing so, learn to apply them in your own projects.
- Have fun.

And more precisely, we are going to build:
- a **Django** web application for... 🥁 taking notes.
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
# Run the migrations in order to apply changes to the database; it gets created if it does not exist
# Create an admin user account with the specified (dummy) email
./manage.py createsuperuser --email user@example.com  # password
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

We will create an app for... 🥁 taking notes.

### See also

- http://wiki.c2.com/?ModelViewController=

## RESTful Services

### What?

Following is a practical explanation of what a [REST](https://en.wikipedia.org/wiki/REST) [API](https://en.wikipedia.org/wiki/API) is (using our notes application as an example):

A **REST API** (Representational State Transfer Application Programming Interface) is a way for your frontend (i.e. Svelte) to communicate with your backend (i.e. Django) through HTTP requests.
Think of it as a contract between frontend and backend that defines how they exchange data.

Here are the key concepts applied to our notes taking app:

#### Resources and Endpoints
```
Your data entities become URLs (endpoints):
- /api/notes/         → all notes
- /api/notes/42/      → specific note with ID 42
- /api/tags/          → all tags
```

#### HTTP Methods (CRUD operations)
```
Each endpoint supports specific operations:
GET     /api/notes/      → Retrieve all notes
POST    /api/notes/      → Create a new note
GET     /api/notes/42/   → Retrieve note 42
PUT     /api/notes/42/   → Update note 42
DELETE  /api/notes/42/   → Delete note 42
```

#### Request/Response Format (usually JSON)
```json
// GET /api/notes/42/
{
    "id": 42,
    "title": "My Note",
    "content": "Some content",
    "tags": [
        {"id": 1, "name": "work"},
        {"id": 2, "name": "important"}
    ],
    "created_at": "2024-01-15T10:30:00Z",
    "updated_at": "2024-01-15T10:30:00Z"
}
```

#### Query Parameters (for filtering/sorting)
```
GET /api/notes/?search=python     → Search notes containing "python"
GET /api/notes/?tag=work          → Filter notes with "work" tag
GET /api/notes/?sort=updated_at   → Sort notes by update date
```

#### Status Codes (response outcomes)
```
200 OK            → Request successful
201 Created       → New note created successfully
400 Bad Request   → Invalid data sent
404 Not Found     → Note doesn't exist
500 Server Error  → Something went wrong on the server
```

#### Example Frontend Usage (Svelte)
```javascript
// Fetching all notes
async function getNotes() {
    const response = await fetch('/api/notes/');
    const notes = await response.json();
}

// Creating a new note
async function createNote(noteData) {
    const response = await fetch('/api/notes/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(noteData)
    });
    const newNote = await response.json();
}
```

**Key Benefits**:
- Stateless: Each request contains all needed information
- Cacheable: Responses can be cached for performance
- Uniform Interface: Consistent way to handle all resources
- Client-Server Separation: Frontend and backend can evolve independently

**Best Practices**:
- Use plural nouns for resources (/notes/ not /note/)
- Nest related resources logically (/notes/42/tags/)
- Use query parameters for filtering/sorting
- Return appropriate status codes
- Include error messages in responses
- Version your API if needed (/api/v1/notes/)

This structure allows your Svelte frontend to interact with your Django backend in a standardized, predictable way, making it easier to develop and maintain your application.

### Why?

_To be discussed during the course._

### How?

We will use [Django Ninja](https://django-ninja.dev/) to add a REST to our Django application.

See the [Django Ninja tutorial](https://django-ninja.dev/tutorial/).
Django Ninja is already installed, you don't need to take care of that.
Simply draw inspiration from the [CRUD example](https://django-ninja.dev/tutorial/other/crud/) and try to adapt it for our notes taking application.

## Single Page Application (SPA)

### What?
### Why?
### How?

We will use [Svelte](https://svelte.dev/) (with [SvelteKit](https://kit.svelte.dev/)) to build a SPA for our notes taking application.

Execute these commands in your terminal in order to install and run the Django app:
```bash
cd svelte-app
# Install the JavaScript/Node dependencies.
npm install
# Run the Svelte app in local.
npm run dev
```

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
