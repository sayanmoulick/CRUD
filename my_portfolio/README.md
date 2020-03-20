sudo apt-get install virtualenv			pip install virtualenv
virtualenv -p /usr/bin/python3.5 djangovenv
source djangovenv/bin/activate
pip install Django
django-admin startproject my_portfolio
cd my_portfolio/
python manage.py runserver localhost:5000
python manage.py startapp sayan_moulick_portfolio
tree
.
├── db.sqlite3
├── manage.py
├── my_portfolio
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-35.pyc
│   │   ├── settings.cpython-35.pyc
│   │   ├── urls.cpython-35.pyc
│   │   └── wsgi.cpython-35.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── sayan_moulick_portfolio
    ├── admin.py
    ├── apps.py
    ├── __init__.py
    ├── migrations
    │   └── __init__.py
    ├── models.py
    ├── tests.py
    └── views.py
pip install djangorestframework
pip install markdown
pip install django-filter
pip install mysqlclient
python manage.py makemigrations sayan_moulick_portfolio
python manage.py migrate sayan_moulick_portfolio

