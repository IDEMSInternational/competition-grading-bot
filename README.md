# Competition grading bot
A chatbot for processing scans/photos from paper-based multiple choice quizzes

## Set up

1. Setting up a new SDAPS project:
Run this command: sdaps setup new_folder example.tex --add folder_images

    where: new_folder: is the folder where the project will be created
    example.tex: Is the latex file that you want to use
	Note here, the "folder_images" is a folder which contains the image which can be used on a questionnaire.
    if you do not want to include the images feel free to remove it(--add folder_images).

    Then if you have the scanned file, you add it on project by the following command

2. Adding scanned file to a project:
Run this command: sdaps add ./project_folder  --convert example-scan.pdf

where: project_folder : is the folder that was created while was setting up a project.
       example-scan.pdf: is the scanned file after the survey or exams


3. Optical Mark recognition:
Run this command: sdaps recognize project_folder/


4. Exporting csv file:
Run this command command:  sdaps csv export project_folder/

where: project_folder is the folder which was created during the project setting up

