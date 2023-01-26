# A Simple To Do List Backend
Backend APIs for a simple To Do App using Django 4.1.5 and Django Rest Framework 3.14.0

## Setup

### 1. Clone the Repo 

``git clone https://github.com/mukesh5/to_do_api.git``

### 2. Create A Virtual Env

``python3 -m venv todo_env``

### 3. Install Requirements

``pip install -r requirements.txt``

### 4. Add your Database Credentials

``DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'DB_NAME',
        'USER': 'DB_USER',
        'PASSWORD': 'DB_PASSWORD',
        'HOST': 'DB_HOST',
        'PORT': 'DB_PORT'
    }
}
``

### 5. Activate Env and Make Migrations

``source ../todo_env/bin/activate``
``python todo_api/manage.py makemigrations``
``python todo_api/manage.py migrate``

### 6. Start the application

``python todo_api/manage.py runserver``


## APIs Endpoints

### 1. Register User
``POST ${HOST}/user/register``

### 2. Login User

``POST ${HOST}/user/login``

### 3. Create a Task for User

``POST ${HOST}/tasks/add``

### 4. Update a Task for User

``PATCH ${HOST}/tasks/update/${task_id}``

### 5. Delete User Task

``DELETE ${HOST}/tasks/delete/${task_id}``

### For API Payload you can download the below postman collection

[POSTMAN_COLLECTION](https://drive.google.com/file/d/1kc1cd8kOM-6iuwElJi9-0pju6xitwTS1/view?usp=sharing)

## Improvements that can be added

#### 1. Setup ENV for SECRET KEYS, DATABASE CREDENTIALS
#### 2. Setup Docker container for the service
#### 3. Add Unit Tests for all the APIs
#### 4. User Sessions should expire after a given amount of time