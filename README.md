
## Getting Started
### Installing Dependencies
#### Python
Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment
I recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies
Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies
- [Django](https://www.djangoproject.com/)  is a backend framework. Django is required to handle requests and responses.

- [Django-rest-framework](https://www.django-rest-framework.org/) Django REST framework is a powerful and flexible toolkit for building Web APIs.


## Running the server
From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:
#### Mac , Linux

```bash

python3 manage.py runserver
```

To run the server, execute:
#### Windows

```bash
python manage.py runserver
```
# Endpoints
## General
#### POST /dj-rest-auth/registration/
* General:
    - Returns Token and user type.
* Request Sample: ``` curl http://ec2-18-191-113-113.us-east-2.compute.amazonaws.com:8000/dj-rest-auth/registration/ -X POST -H "Content-Type: application/json" -d
            '{
                "username": "name",
                "password1":"Aa123456789",
                "password2":"Aa123456789",
                "email":"name@gmail.com",
                "user_type":"1"
                }' 
            ```
* Response Sample:
```sh
{
    "key": "52862e084f56792e2644b1801952a728a75fd8e5",
    "user_type": 1
}
```
#### POST /dj-rest-auth/login/
* General:
    - Returns Token and user type.
* Request Sample: ``` curl http://ec2-18-191-113-113.us-east-2.compute.amazonaws.com:8000/dj-rest-auth/login/ -X POST -H "Content-Type: application/json" -d
            '{
            "username": "name",
            "password":"Aa123456789"
            }' 
            ```
* Response Sample:
```sh
{
    "key": "bd5188970056063a94afcf859820713f8cab743e",
    "user_type": 2
}
```