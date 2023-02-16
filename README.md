# Django Template

Django Template is a simple Django app that comes equipped with a landing page, authentication functionality, and a dashboard.

It was designed to save developers time and frustration when creating new Django applications, by providing a pre-built foundation with some of the most common features already in place.

## Features

This Django Template project is extremely barebones and comes with three pre-configured apps: **landing_page**, **accounts**, and **dashboard**.

  1. **landing_page** - serves as the homepage for your application and can be customized further to fit your needs.
  2. **accounts** - adds user registration, login and logout functionality to your application.
  3. **dashboard** - the app where your users are directed after logging in/registering. Your app functionality can be added here.
  
## Setup

To begin using this template, start by cloning the repository from Github:

    git clone git@github.com:michael-awe/django-template.git

Next, cd into the directory and create a virtual environment

    cd django-template
    python3 -m venv env
    source env/bin/activate

Now install the dependencies from requirements.txt

    pip install -r requirements.txt

After the requirements finish installing, run setup.sh and when prompted, enter a new project name:

    sh setup.sh
    ...
    Enter a new project name: (ensure name is allowed by Django before pressing enter)

**NOTE: Ensure that the project name you enter is unique to ensure no clashes with Django or other Python modules**

## Usage

After installing Django Template, you can use it as a starting point for your Django application. You can customize the landing page, authentication, and dashboard apps to fit the specific needs of your application. The pre-built foundation provides a solid starting point that you can build on top of, without having to start from scratch.

## Contributing

If you would like to contribute or notice some inconsistencies in the code, please fork the project, make your changes, and submit a pull request. Any contributions that improve the functionality or usability of the project are welcome.

## License

Django Template is licensed under the MIT License, which means that you are free to use, modify, and distribute the project as you see fit. See the LICENSE file for more information.
