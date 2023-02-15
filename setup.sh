#Install dependencies
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

#Make database migrations
python manage.py makemigrations && python manage.py migrate

#Renames project
echo "Enter a new project name: (ensure name is allowed by Django before pressing enter)"
read project_name
python rename.py $project_name

#Clean up
rm rename.py

#Run server
python manage.py runserver