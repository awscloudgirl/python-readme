from InquirerPy import prompt
from rich.console import Console
from rich.markdown import Markdown

def get_project_details():
    questions = [
        {"type": "input", "name": "title", "message": "Enter your project title:"},
        {"type": "input", "name": "description", "message": "Describe your project:"},
        {"type": "input", "name": "installation", "message": "Installation instructions:"},
        {"type": "input", "name": "usage", "message": "Usage instructions:"},
        {"type": "list", "name": "license", "message": "Choose a license:",
         "choices": ["MIT", "Apache 2.0", "GPL v3", "LGPL v3", "MPL 2.0", "Creative Commons", "Unlicense"]},
        {"type": "input", "name": "author", "message": "Author contact information:"}
    ]
    return prompt(questions)

def create_readme(details):
    readme_content = f"""
# {details['title']}

## Description
{details['description']}

## Installation
{details['installation']}

## Usage
{details['usage']}

## License
This project is licensed under the {details['license']} License.

## Author
{details['author']}
    """
    with open("README.md", "w") as file:
        file.write(readme_content)

    console = Console()
    console.print(Markdown("# README.md created successfully!"), style="bold green")

def main():
    details = get_project_details()
    create_readme(details)

if __name__ == "__main__":
    main()
