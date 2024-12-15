import subprocess
import os

def push_to_github(folder_path, repo_url, commit_message):
    try:
        # Change directory to the folder
        os.chdir(folder_path)

        # Initialize git repository if not already initialized
        subprocess.run(["git", "init"], check=True)

        # Add remote repository
        subprocess.run(["git", "remote", "add", "origin", repo_url], check=False)

        # Add all files to the staging area
        subprocess.run(["git", "add", "--all"], check=True)

        # Commit the changes
        subprocess.run(["git", "commit", "-m", commit_message], check=True)

        # Set branch to main
        subprocess.run(["git", "branch", "-M", "main"], check=True)

        # Push changes to GitHub
        subprocess.run(["git", "push", "-u", "origin", "main"], check=True)

        print("Folder successfully pushed to GitHub repository.")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Example usage
folder_path = r"D:\Sonali_AI_Projects\Woxsen_Projects\Negotiation_Course_Chatbot"  # Replace with the folder path you want to push
repo_url = "https://github.com/woxsenailab/Woxsen_Courses_Chatbots.git"  # Replace with your repository URL
commit_message = "Initial commit"  # Customize your commit message

push_to_github(folder_path, repo_url, commit_message)