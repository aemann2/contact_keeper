# [Django Contact Keeper](https://django-contact-keeper.herokuapp.com/)

<a href="https://django-contact-keeper.herokuapp.com/" target="_blank"><img src='https://user-images.githubusercontent.com/68879246/183273949-fc64ab50-e5fd-450b-b0ec-ea9ac3f9fb7b.png' alt='Django Contact Keeper'></a>

**Contact Keeper** is an application built with Django. This is a full stack application that allows a user to register and create contacts with phone and email info, as well as filter those contacts. This project is a Django adaptation of Brad Traversy's React Contact Keeper, taken from his React Front to Back Udemy course.

**_Demo login credentials:_**
**Username**: testUser
**Password**: 123test123

## Running the project locally
- Clone or download the repo (e.g, `gh repo clone aemann2/contact_keeper`)
- Place the cloned repo in a directory. I call mine `djago_contact_keeper`
- Set up a virtual environment using `python -m venv venv`
- Activate the virtual environment using `. venv/bin/activate` with bash, or using `source venv/bin/activate` with zsh
- Navigate into the main `contact_keeper` directory
- In the `contact_keeper`, install the project dependencies using `pip install -r requirements.txt`
- Follow the directions [here](https://dev.to/mungaigikure/how-to-set-up-postgres-in-your-django-project-575i) to set up a Postgres database locally
- In the main `contact_keeper` directory, run `python manage.py migrate`
- Navigate to the `src` directory and create a file called `.env`. Populate this file with the values used to set up your Postgres database. Make sure `DEBUG` is set to `TRUE`.
- In the main `contact_keeper` directory, run `python manage.py runserver` to run the project locally


## Commands for running tests w/ coverage: 
- Run test suite: `coverage run --source='.' manage.py test`
- Building HTML page for coverage results: `coverage html`