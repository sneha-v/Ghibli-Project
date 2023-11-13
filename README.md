# Ghibli-Project

This project aims to create a project utilizing Django and DRF to create an endpoint to get a list of movies and people in them.
This project uses **Caching - PyMemcached** in order to avoid delay in response for the users.

## Setup
The first thing to do is to clone the repository:

```properties
$ git clone https://github.com/sneha-v/Ghibli-Project.git
$ cd Ghibli-Project
```

Create a virtual environment to install dependencies in and activate it:
```properties
$ python -m venv env
$ source env/bin/activate
```
Then install the dependencies:
```properties
(env)$ pip install -r requirements.txt
```

Once pip has finished downloading the dependencies:
```properties
(env)$ python manage.py migrate
(env)$ python manage.py runserver
```
And navigate to http://127.0.0.1:8000/list_movies/ 

## Authorization
To Authorize and get list of movie you need to set up Authorization header.

```properties
Authorization: Api-Key <API-KEY>
```
Will be sending out the api key through mail.

## Tests
Requirement - set up the apikey in the GHIBLI_KEY enviroment variable
To run the tests, cd into the directory where manage.py is:
```properties
(env)$ python manage.py test
```

## Note
Movie list is cached for 60 seconds and the actors list is cache for 24 hours (can be increased based on the required scenario)

Haven't set up DB for based on current scenario but the decision would change if there is a change in requirement. 