
# Competition grading bot
    A chatbot for processing scans/photos from paper-based multiple choice quizzes

## Set up

    Make sure you have sdaps installed on your Ubuntu os

 ### SDAPS Installation

    ####### sudo add-apt-repository ppa:benjamin-sipsolutions/sdaps or /sdaps-unstable
    ####### sudo apt-get update
    ####### sudo apt-get install sdaps 


### 1. Setting up a new SDAPS project:
###### Run this command: sdaps setup new_folder example.tex --add coins

        where: new_folder: is the folder where the project will be created
        example.tex: Is the latex file that you want to use
        Note here, the "coins" is a folder which contains the image which can have been used on a questionnaire during latex creation.
        if you do not want to include the images feel free to remove it(--add folder_images /coins).

        Then if you have the scanned file, you add it on project with the following command

### 2. Adding scanned file to a project:
###### Run this command: sdaps add ./project_folder  --convert example-scan.pdf

        where: project_folder : is the folder that was created while was setting up a project.
        example-scan.pdf: is the scanned file after the survey or exams


### 3. Optical Mark recognition:
###### Run this command: sdaps recognize project_folder/


### 4. Exporting csv file:
###### Run this command :  sdaps csv export project_folder/

        where: project_folder is the folder which was created during the project setting up

        If you are using the set up as mine, then you will have to run the setup by this command:
        python3 sdaps_tools.py

