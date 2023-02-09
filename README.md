# Competition grading bot
    A chatbot for processing scans/photos from paper-based multiple choice quizzes

## Set up

    Make sure you have sdaps installed on your Ubuntu os

### SDAPS Installation

    ####### sudo add-apt-repository ppa:benjamin-sipsolutions/sdaps or /sdaps-unstable
    ####### sudo apt-get update
    ####### sudo apt-get install sdaps 

## Usage

### Setting up project from a single .tex file

`python3 main.py setup_project project_id tex_file`

### Parsing a single image (and printing output)

`python3 main.py setup_project project_id image_file`

### Deleting a project

`python3 main.py delete_project project_id`
