
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
    - Returns Token 
* Request Sample: ``` curl http://127.0.0.1:8000/dj-rest-auth/registration/
            '{
                "username": "name",
                "password1":"Aa123456789",
                "password2":"Aa123456789",
                "email":"name@gmail.com",
                }' 
            ```
* Response Sample:
```sh
{
    "key": "52862e084f56792e2644b1801952a728a75fd8e5",
}
```
#### POST /dj-rest-auth/login/
* General:
    - Returns Token and user type.
* Request Sample: ``` curl http://127.0.0.1:8000/dj-rest-auth/registration/
            '{
            "username": "name",
            "password":"Aa123456789"
            }' 
            ```
* Response Sample:
```sh
{
    "key": "bd5188970056063a94afcf859820713f8cab743e",
}
```
#### GET http://127.0.0.1:8000/products
* General:
    - Returns all products.
* Request Sample: ``` curl http://127.0.0.1:8000/products
       
* Response Sample:
```sh
[{"id":1,"name":"Shampoo","seller":"Sami","price":"80.00","user":4},{"id":2,"name":"Short","seller":"Sami","price":"54.00","user":8}]
```

#### POST http://127.0.0.1:8000/products
* General:
    - Post product.
* Request Sample: ``` curl http://127.0.0.1:8000/products


          {"name":"Shampooll","seller":"Sami","price":"80.00","user":4}
         
* Response Sample:
```sh
{"message":{"id":5,"name":"Shampooll","seller":"Sami","price":"80.00","user":4}}
```

#### GET http://127.0.0.1:8000/userproducts/<int:pk>/
* General:
    - Get user products .
* Request Sample: ``` curl http://127.0.0.1:8000/userproducts/4/

         {"name":"Shampooll","seller":"Sami","price":"80.00","user":4} 
            
* Response Sample:
```sh
[{"id":1,"name":"Shampoo","seller":"Sami","price":"80.00","user":4},{"id":3,"name":"Shampoos","seller":"Sami","price":"80.00","user":4},{"id":4,"name":"Shampooss","seller":"Sami","price":"80.00","user":4},{"id":5,"name":"Shampooll","seller":"Sami","price":"80.00","user":4}]
```

