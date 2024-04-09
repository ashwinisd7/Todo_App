This is a simple Django application for managing todo lists.

The Django Todo App is a simple web application built with Django, designed to help users manage their todo lists efficiently. It provides a user-friendly interface for adding, updating, and deleting tasks, as well as marking them as completed.

Features

Task Management: Users can create, view, update, and delete tasks.
Due Dates: Each task can have an associated due date.
Task Status: Tasks can be marked as completed or pending.
User Interface: Clean and intuitive interface for easy task management.

Usage

Navigate to the homepage to view the list of tasks.
Click on "Add Task" to create a new task.
Enter task details and select a due date.
Click "Save" to add the task.
To mark a task as completed, click on the checkbox next to the task.
To delete a task, click on the delete button next to the task.

Installation:

Create environment: python -m venv myvenv
Start environment: myvenv/Scripts/activate
Create Project: djano-admin startproject demo
Create App: djando-admin startapp demoapp 
Create Superuser: python manage.py createsuperuser 
Go to Settings and add demoapp in installed apps
In the demo/urls add the urls for demoapp/urls
Create demoapp/templates/demoapp/index.html
Create the model todoitem for todolist
Create a form for submission in demoapp/forms.py
Create view for rendering the main page
Register the model on admin.
Create Migrations: python manage.py makemigrations
Execute Migrations: python manage.py migrate
Run application: python manage.py runserver


