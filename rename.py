import os
import sys

# Get the old and new project names from the command line arguments
old_project_name = sys.argv[1]
new_project_name = sys.argv[2]

# Rename the project directory
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