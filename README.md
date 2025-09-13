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