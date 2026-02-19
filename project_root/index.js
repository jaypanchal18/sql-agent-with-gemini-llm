import os

def create_project_structure():
    try:
        # Define the project root directory
        project_root = 'project_root'
        
        # Define the directories to be created
        directories = [
            os.path.join(project_root, 'app'),
            os.path.join(project_root, 'app', 'templates'),
            os.path.join(project_root, 'app', 'static'),
            os.path.join(project_root, 'config'),
            os.path.join(project_root, 'migrations'),
            os.path.join(project_root, 'tests'),
            os.path.join(project_root, 'venv')
        ]
        
        # Create the directories
        for directory in directories:
            os.makedirs(directory, exist_ok=True)
        
        print("Project structure created successfully.")
    
    except Exception as e:
        print(f"An error occurred while creating the project structure: {e}")

if __name__ == "__main__":
    create_project_structure()