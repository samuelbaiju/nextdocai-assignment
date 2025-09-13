# Project & Task Management Application

This is a Django-based application for managing projects and tasks. It includes a REST API, automated task management with Celery, and a customized Django Admin interface.

## Features

- **Project and Task Management**: Define projects and different types of tasks (e.g., Development, Design).
- **RESTful API**: CRUD endpoints for projects and tasks with filtering support.
- **Automated Tasks**: Celery automatically marks tasks as overdue and handles notifications.
- **Custom Admin Interface**: Manage projects and tasks with inline editing, filters, and bulk actions.
- **Signals**: Automatic task deletion on project removal and notifications on task creation.

## Setup Instructions

### 1. Clone the repository


git clone https://github.com/samuelbaiju/nextdocai-assignment.git
cd project_management

3. Install dependencies
Install the required Python packages.
pip install -r requirements.txt


4. Configure the database
By default, the project uses SQLite. You don't need to do anything, but if you want to use a different database, update project_management/settings.py.

5. Run migrations
Apply the database schema changes.

python manage.py makemigrations
python manage.py migrate


6. Create a superuser
Create an admin user to access the Django Admin site.

python manage.py createsuperuser


7. Run the development server
python manage.py runserver
You can now access the API at http://127.0.0.1:8000/api/ and the Admin site at http://127.0.0.1:8000/admin/.

8. Run Celery workers
Start a Celery worker to process tasks and a Celery Beat scheduler for periodic tasks.


# Start the Redis server (if not already running)
# Start the Celery worker
celery -A project_management worker -l info
# Start Celery Beat for scheduled tasks
celery -A project_management beat -l info
Running Tests
To ensure everything is working correctly, run the test suite.

python manage.py test management