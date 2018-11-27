# BriteCore - Product Development - Challenge submission


This is the repository containing my submission for the Software developer (Product development) position at BriteCore.
The backend is implemented with Django and Django Rest Framework, while the frontend is implemented in VueJS + Vuex.

### Extended list of technologies used include:
- Python
- Javascript
- Django
- Django Rest Framework
- PostgreSQL
- MongoDB
- VueJS
- Vuex
- Bootstrap
- AWS Lambda
- Netlify

## Backend approach
The backend is implemented in Django and Django Rest Framework. I implemented three django models for the challenge's business logic: RiskType, RiskField, and RiskFieldOption. Their relationships are described in the ER diagram on the image below:

![alt text](https://i.imgur.com/5KKjpTU.png "ER Diagram of the 3 mentioned models")

## Frontend approach
The frontend is implemented in VueJS, also using Vuex for state management. Frontend project boilerplate was generated using vue-cli

## Running the project locally
### Backend
- Clone this repository: `git clone https://github.com/LejlaKusari/InsuranceApp.git`
- Change directory to InsuranceApp: `cd InsuranceApp`
- Create virtual environment: `virtualenv -p python3 venv`
- Install dependencies: `pip install -r requirements.txt`
- Setup a postgres database on your system and edit the databases portion in `settings.py` according to your setup
- Run migrations: `./manage.py migrate`
- Start local server: `./manage.py runserver`
- The backend api is now up and running at `http://localhost:8000`
### Frontend
- Change directory to frontend: `cd frontend`
- Install dependecies: `npm install`
- Start local frontend server: `npm run serve`
- The frontend implementation is now up and running at `http://localhost:8080`

## Deployment
The backend api is deployed in AWS Lambda, with the help of Zappa and Zappa Django Utils: the endpoints available are listed below:
- GET : https://4jsq8d101c.execute-api.us-east-2.amazonaws.com/prod/risks/:pk - Retrieve a single risk model through it's primary key
- GET: https://4jsq8d101c.execute-api.us-east-2.amazonaws.com/prod/risks/list - List a list of risk models, ordered by last created, paginated
- POST: https://4jsq8d101c.execute-api.us-east-2.amazonaws.com/prod/risks/create/ - Create a new risk model
- POST: https://4jsq8d101c.execute-api.us-east-2.amazonaws.com/prod/risks/entry/ - Create a new entry for a particular risk model

The frontend is deployed in Netlify and is currently live at: `https://paste-link-here.com`
