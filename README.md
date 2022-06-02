
# E-Learning Management System

![](https://img.shields.io/badge/python-3.10-red) ![](https://img.shields.io/badge/django-v4.0.4-blue) ![](https://img.shields.io/badge/bootstrap-v5.2.0-success)   ![](https://img.shields.io/github/license/nz-m/django-eLMS)

### Project Overview

Currently implemented features:
- **Admin** manages all the courses, create student and teacher accounts, and assign courses to teachers.
- **Student** can enroll in courses with the enrollment key, view course content, and submit assignments.
- **Teacher** can view course content, post announcement and course content, create assignments, and grade assignments.

    Each course has discussion channels for both students and teachers.

### Tech Stack
Django 4.0.4

Bootstrap 5

MySQL Database

## Relational Schema
![](https://raw.githubusercontent.com/nz-m/django-eLMS/main/img/Schema.png)




## Installation
Clone the repository into your local machine

```sh
git clone https://github.com/nz-m/django-eLMS.git
```
Install python virtual evironment (windows):

```sh
pip install virtualenv
```
cd into the project directory. Create a virtual environment and activate it

```sh
virtualenv env
```
```sh
env\Scripts\activate
```
Install the dependencies

```sh
pip install -r requirements.txt
```
### Setting up the MySQL Database

>MySQL was used during the development and currently is configured to use MySQL. You can use the sqlite3 which comes with Django by default. Skip the following steps in that case. To use sqlite uncomment the sqlite configuration in the `settings.py` file and remove the MySQL configuration.

If you have MySQL installed create a new database or [download](https://dev.mysql.com/downloads/):

```sh
mysql -u root -p
```
```sh
CREATE DATABASE elms;
```

Then in the `settings.py` file, change the `DATABASES` configuration accordingly.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'elms',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': '',
    }
}
```
Create migrations and migrate

```sh
python manage.py makemigrations
```
```sh
python manage.py migrate
```
Create a superuser

```sh
python manage.py createsuperuser
```
Finally, run the project

```sh
python manage.py runserver
```
Now the server should be running on http://127.0.0.1:8000/

Go to the admin panel, add some courses, create some students and teachers, and assign them to courses.

## User Interface
**Student Dashboard**

![](https://raw.githubusercontent.com/nz-m/django-eLMS/main/img/student%20dashboard.png)
**Student Course Page**

![](https://raw.githubusercontent.com/nz-m/django-eLMS/main/img/student%20course%20page.png)
**Student assignment portal**

![](https://raw.githubusercontent.com/nz-m/django-eLMS/main/img/student%20assignment%20portal.png)
**Teacher course page**

![](https://raw.githubusercontent.com/nz-m/django-eLMS/main/img/teacher%20course%20page.png)
**Teacher assignment portal**

![](https://raw.githubusercontent.com/nz-m/django-eLMS/main/img/teacher%20assignment%20portal.png)
**Discussion channel**

![](https://raw.githubusercontent.com/nz-m/django-eLMS/main/img/discussion.png)


## License
[The MIT License (MIT)](https://github.com/nz-m/django-eLMS/blob/main/LICENSE)













