from django.core.management.base import BaseCommand
import os
import sys

class Command(BaseCommand):
    help = "Renames your Django project. Note this method was not intended for use after initial project setup."
    
    def add_arguments(self, parser):
        parser.add_argument('old_project_name', type=str, help='The current project name')
        parser.add_argument('new_project_name', type=str, help='The new project name')
    
    def handle(self, *args, **kwargs):
        print("Renaming your Django project...")

        # Get the old and new project names from the command line arguments
        old_project_name = kwargs['old_project_name']
        new_project_name = kwargs['new_project_name']
        
        print(f"Renaming {old_project_name} to {new_project_name}...")
        
        #Rename the project directory
        os.rename(old_project_name, new_project_name)

        # Iterate through all files in the project directory and its subdirectories
        for root, dirs, files in os.walk(new_project_name):
            for file in files:
                file_path = os.path.join(root, file)

                try:
                    # Open the file for reading
                    with open(file_path, 'r') as f:
                        file_contents = f.read()

                    # Replace all occurrences of the old project name with the new project name
                    file_contents = file_contents.replace(old_project_name, new_project_name)

                    # Open the file for writing and write the modified contents
                    with open(file_path, 'w') as f:
                        f.write(file_contents)
                except:
                    pass

        #renames the project name in the manage.py file
        with open(f"./manage.py", 'r') as f:
            file_contents = f.read()

            # Replace all occurrences of the old project name with the new project name
            file_contents = file_contents.replace(f'{old_project_name}', f'{new_project_name}')

            # Open the file for writing and write the modified contents
            with open(f"./manage.py", 'w') as f:
                print("writing to file")
                f.write(file_contents)

        # Print a message indicating that the project has been renamed
        print(f"{old_project_name} has been renamed to {new_project_name}.")