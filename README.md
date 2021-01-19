# Capstone

## Casting Agency Specifications

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

## Motivation for project

As the end of the nanoDegree program, we need to create a project where we demonstrate the skills we studded.

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip3 install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

## Database Setup

Creating a database using the migrations file provided. From the main folder in terminal run:

```bash
flask db init
```
and then run:
```bash
flask db migrate 
```


## Running the server

From within the directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
. ./setup.sh
flask run --reload
```

#### Flask run tests with token headers set in the setup.sh file. If they have expired, please login using the credentials below and replace them in setup.sh and run setup.sh again

setup.sh has all the environment variables needed for the project. The app may fail if they are not set properly. If that happens just copy paste lines from setup.sh on you CLI.

###### To test live APIs use Postman requests. Add Auth token headers from logins below to test.

Auth0 login url:

https://dev-exc8ii15.us.auth0.com/authorize?audience=cap&response_type=token&client_id=ECTG0uBj6b6Y7frXy7LrZEBdSR7AmW2P&redirect_uri=https://127.0.0.1:5000/result

There is 3 accounts for the 3 roles in the API:

1- Casting Assistant
casting Assistant username: as@a.com Password: 055914099Kk
2- Casting director
Casting director username: aa@aa.com 055914099Kk
3- Executive Producer
Executive Producer username: az@az.com 055914099Kk


# Project deployed at

https://fsnd-capstone1.herokuapp.com/

## Testing

To run the tests, run

```
python test_app.py
```


#### The tests uses the tokens in the setup.sh please update the tokens.



## API Reference

### Error Handling

Errors are returned as JSON objects in the following format:

```
{
    "success": False,
    "error": 404,
    "message": "Resource not found"
}

```

### Endpoints

GET '/movies'
GET '/movies/<movie_id>'
GET '/actors'
GET '/actors/<actor_id>'
DELETE '/movies/<movie_id>'
DELETE '/actors/<actor_id>'
POST '/movies'
POST '/actors'
PATCH '/movies/<movie_id>'
PATCH '/actors/<actor_id>'


GET '/movies'
Fetches an array of movies
Success Response:

```
{
   "success":True,
   "movies":[
      {
         "id":2,
         "release_date":"1999-01-01",
         "title":"my life"
      }
   ]
}
```

GET '/movies/<movie_id>'
Fetches an array of actors
Success Response:

```
  {
   "success":True,
   "movie":[
      {
         "id":2,
         "release_date":"1999-01-01",
         "title":"my life"
      }
   ]
}
```

GET '/actors'
gets all actors in the database
Success Response:

```
{
   "success":True,
   "actor":{
      "id":10,
      "age":30,
      "gender":"male",
      "name":"abdullah"
   }
}
```

GET '/actors/<actor_id>'
get an actor by id
Returns:json
Success Response:

```
{
   "success":True,
   "actor":{
      "id":10,
      "age":30,
      "gender":"male",
      "name":"abdullah"
   }
}
```

DELETE '/movies/<movie_id>'
Delete a movie in the database.
Success Response:

```
{
    'success': True,
    'delete': movie_id
}
```

DELETE '/actors/<actor_id>'
Delete an actor in the database.
Success Response:

```
{
    'success': True,
    'delete': actor_id
}
```

POST '/movies'
post a movie to the database
Success Response:

```
{
   "success":True,
   "movie":{
      "id":2,
      "release_date":"1999-01-01",
      "title":"my life"
   }
}
```

POST '/actors'
Post an actor in the database
Success Response:

```
{
   "success":True,
   "actor":{
      "age":30,
      "gender":"male",
      "id":2,
      "name":"abdullah"
   }
}
```

PATCH '/movies/<movie_id>'
Edit a movie in the database
Success Response:

```
{
   "success":True,
   "movie":{
      "id":2,
      "release_date":"1999-01-01",
      "title":"my life"
   }
}
```

PATCH '/actors/<actor_id>'
Edit an actor in the database
Success Response:

```
{
   "success":True,
   "actor":{
      "age":30,
      "gender":"male",
      "id":2,
      "name":"abdullah"
   }
}
```
## Authors

Abdullah Alfadhel and udacity team provided the starter code.