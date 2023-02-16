#Make database migrations
python manage.py makemigrations && python manage.py migrate

#Renames project
echo "Enter a new project name: (ensure name is allowed by Django before pressing enter)"
read project_name
sudo python3 rename.py 'djangotemplate' $project_name

#Clean up
rm rename.py

#Run server
python manage.py runserver