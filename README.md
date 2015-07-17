## Setup

Install `git` and clone the GitHub repository:

    $ sudo apt-get install git
    $ git clone https://github.com/MissFilly/scatchbling.git

Install system-wide dependencies:

    $ sudo apt-get install python-dev python-virtualenv

Install Heroku Toolbelt:

    $ wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh

Use `virtualenv` and install required packages:

    $ cd scatchbling
    $ virtualenv env
    $ source env/bin/activate
    $ pip install -r requirements.txt

Create an `.env` file with content (you can generate a Django secret
key [here](http://www.miniwebtool.com/django-secret-key-generator/):

    DATABASE_URL="sqlite:////path/to/db.sqlite3"
    SECRET_KEY="your_django_secret_key"

Migrate:

    $ foreman run ./manage.py migrate

Run the development server:

    $ foreman run ./manage.py runserver

Now you can access the application in `http://localhost:8000`.