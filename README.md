## Thread Website Re-launch 2018

##### Tools used:

* Django
* Bootstrap
* SQLlite
* Sass

##### Virtual Environment Set-up:
~~~~
pip3 install virtualenv

virtualenv venv

source venv/bin/activate

pip3 install -r requirements.txt
~~~~

#### Sass Set-up:
~~~
# Change Directory into scss
# run this every time you or someone else makes a change to css
sass --watch scss:css
~~~

#### Django Backend
~~~
# when installing backend for first time
python3 manage.py migrate --run-syncdb

# to run on http://localhost:8000
python3 manage.py runserver

# when making backend changes


#Change your models (in models.py)
python3 manage.py makemigrations #to create migrations for those changes
python3 manage.py migrate #to apply those changes to the database.

# running shell for db interaction
python3 manage.py shell
~~~

#### Front-End

~~~
tbd
~~~
