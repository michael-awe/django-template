# modified from original implementation

echo "Project setup begun."

#Make database migrations
python manage.py makemigrations && python manage.py migrate
echo "Migration successful."

#Install tailwind dependencies
python manage.py tailwind install
echo "Tailwind install successful."

echo "Project setup complete."