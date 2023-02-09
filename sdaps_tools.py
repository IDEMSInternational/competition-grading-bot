import subprocess
import csv
import shutil
import os


def setup_sdaps_project(tex_file, project_id, data_folder=''):
    # TODO: Fill in code that sets up an SDAPS project for the given tex
    # file and with the given project id (=sdaps folder name).

    folder_path = os.path.join('./assets/results/', project_id)

    #The command for setting up sdaps project
    create_project_command = ['sdaps', 'setup', folder_path, tex_file]
    if data_folder:
        create_project_command += ['--add', data_folder]
    subprocess.run(create_project_command)

    shutil.copyfile(os.path.join(folder_path, "survey.sqlite"), os.path.join(folder_path, "survey_blank.sqlite"))

    return project_id
    

def delete_sdaps_project(project_id):
    shutil.rmtree(os.path.join('./assets/results/', project_id))


def parse_image(image, project_id):
    # Invokes SDAPS to process the image into a text format (e.g. csv).
    # Reads the output and prints it to the screen.

    folder_path = os.path.join('./assets/results/', project_id)
    # Reset the DB
    shutil.copyfile(os.path.join(folder_path, "survey_blank.sqlite"), os.path.join(folder_path, "survey.sqlite"))

    # accepting the scanned image
    scanned_images_command=['sdaps', 'add', folder_path, '--convert', image]
    subprocess.run(scanned_images_command)

    #Run Optical mark recognition
    recoginize_image_command=['sdaps', 'recognize', folder_path]
    subprocess.run(recoginize_image_command)

    # # reporting csv result
    changing_csv_report=['sdaps', 'csv', 'export', folder_path]
    subprocess.run(changing_csv_report)
    
    # TODO: get the actual output and print it (student answers and other info).
    csv_path = os.path.join(folder_path, 'data_1.csv')
    with open(csv_path, 'r') as file:
        reader = csv.DictReader(file)
        row = next(reader)
    os.remove(csv_path)
    os.remove(os.path.join(folder_path, '1.tif'))
    return row
