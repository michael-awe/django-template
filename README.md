# Django Template

Django Template is a simple Django app that comes equipped with a **landing page**, **authentication** functionality, and a **dashboard**. It also comes fully integrated with **django-auto-reload** for hot reload functionality during development and **django-tailwind** so you can start using TailwindCSS straight away.

It was designed to save developers time and frustration when creating new Django applications by providing a pre-built foundation with some of the most common features already in place.

## Features

This Django template is extremely barebones and comes with three pre-configured apps: **landing_page**, **accounts**, and **dashboard**.

  1. **landing_page** - serves as the homepage for your application and can be customized further to fit your needs.
  2. **accounts** - adds user registration, login and logout functionality to your application.
  3. **dashboard** - the app where your users are directed after login/registration. Your app functionality can be added here.

Additionally, the template comes with the following Python packages pre-installed:

  1. [**django-auto-reload**](https://github.com/adamchainz/django-browser-reload) - This provides your app with hot reload functionality to make development so much easier
  2. [**django-tailwind**](https://django-tailwind.readthedocs.io/en/latest/installation.html) - This provides out of the box support for TailwindCSS
  
## Requirements

To use this template you'll need to have the following installed:

  1. Python 3
  2. Latest version of NodeJS (https://nodejs.org/en)

## Setup

To begin using this template, start by creating a directory for your project:

    mkdir <YOUR_PROJECT_NAME>
    cd <YOUR_PROJECT_NAME>

Clone the repository into the current directory:

    git clone git@github.com:michael-awe/django-template.git .

Next, create and activate a virtual environment

    python3 -m venv env
    source env/bin/activate

Now install the dependencies from requirements.txt

    pip install -r requirements.txt

After installing the requirements, run setup.sh. When prompted, enter a new project name:

    sh setup.sh
    python manage.py tailwind install
    ...
    Enter a new project name: (ensure name is allowed by Django before pressing ENTER)

**NOTE: Ensure that the project name you enter is unique to ensure no clashes with Django or other Python modules**

## Usage

In order to use Tailwind, you'll have to create two terminal tabs, one to start tailwind and the other to start your Django server

In the first terminal type:

    python manage.py tailwind start

You can then start your Django server in a separate tab like this:

    python manage.py runserver

You're now all set and ready to start developing!

### Adding Tailwind to additional templates

By default, the landing_page, accounts and dashboard apps all have Tailwind integrated in their respective base.html files. 

However, if you'd like to create a new app and add Tailwind support, either inherit from the base.html files of the other apps or add the following tags to your new HTML templates:

```
{% load static tailwind_tags %}
...
<head>
   ...
   {% tailwind_css %}
   ...
</head>
```



## Contributing

If you would like to contribute to this repository or notice any issues with the code, please feel free to fork this repository and submit your changes in a pull request. Any contributions that improve the functionality or usability of the project are welcome.

## License

Django Template is licensed under the MIT License, which means that you are free to use, modify, and distribute the project as you see fit. See the LICENSE file for more information.
