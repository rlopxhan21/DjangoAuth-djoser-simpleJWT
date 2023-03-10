# Django Authentication with Simple JWT and djoser

A simple django API endoints for authentication using djoser and simpleJWT packages 

## How to install:
In terminal:

```
git clone https://github.com/rlopxhan21/DjangoAuth-djoser-simpleJWT.git
```


After the clone is successful, open terminal in project folder:
Run following command for creating virtual env and installing all the required dependencies.

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

And also create a file .env in project folder and store SECRET_KEY.

To run:

```
python manage.py runserver
```

## API Documentation

The API documentation can be found in http://localhost:8000/swagger/, http://localhost:8000/swagger.json/,  http://localhost:8000/redoc/

![image info](docs/api1.png "a title")
![image info](docs/api2.png "a title")