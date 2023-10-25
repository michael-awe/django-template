#Make database migrations
python manage.py makemigrations && python manage.py migrate

#Renames project
echo "Enter a new project name: (ensure name is allowed by Django before pressing enter)"
read project_name
python manage.py rename 'djangotemplate' $project_name

#Run server
python manage.py runserver

#Install tailwind dependencies
python manage.py tailwind install

echo "Project setup complete."