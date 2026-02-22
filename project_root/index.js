import os

def create_project_structure():
    directories = [
        'project_root/',
        'project_root/app/',
        'project_root/app/api/',
        'project_root/app/models/',
        'project_root/app/config/',
        'project_root/app/static/',
        'project_root/app/templates/',
        'project_root/tests/',
        'project_root/migrations/',
        'project_root/venv/',
    ]

    for directory in directories:
        try:
            os.makedirs(directory, exist_ok=True)
        except Exception as e:
            print(f"Error creating directory {directory}: {e}")

    # Create __init__.py files to mark directories as packages
    init_files = [
        'project_root/app/__init__.py',
        'project_root/app/api/__init__.py',
        'project_root/app/models/__init__.py',
        'project_root/app/config/__init__.py',
        'project_root/tests/__init__.py',
    ]

    for init_file in init_files:
        try:
            with open(init_file, 'w') as f:
                f.write("# This file marks the directory as a Python package\n")
        except Exception as e:
            print(f"Error creating file {init_file}: {e}")

if __name__ == "__main__":
    create_project_structure()