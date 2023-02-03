import subprocess
import csv
import argparse
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

    return project_id
    

def parse_image(image, project_id):
    # Invokes SDAPS to process the image into a text format (e.g. csv).
    # Reads the output and prints it to the screen.

    folder_path = os.path.join('./assets/results/', project_id)

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
    with open(os.path.join(folder_path, 'data_1.csv'), 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def main():
    description = 'Write something here.\n\n'
    parser = argparse.ArgumentParser(description=description, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('command', 
            choices=["setup_project", "parse_image", "delete_project"],
            help='Some text here.\n')
    parser.add_argument('project_id', help='ID/name of the project')
    parser.add_argument('input', nargs='?', help='Filename of the .tex file or scan image')
    # parser.add_argument('output', help='Filename')
    parser.add_argument('--image_folder', help='Folder with images referenced by the .tex.')
    args = parser.parse_args()

    if args.command == 'setup_project':
        if not args.input:
            print("input parameter required")
            return
        setup_sdaps_project(args.input, args.project_id, args.image_folder)
    elif args.command == 'delete_project':
        shutil.rmtree(os.path.join('./assets/results/', args.project_id))
    elif args.command == 'parse_image':
        if not args.input:
            print("input parameter required")
            return
        parse_image(args.input, args.project_id)
    

if __name__ == "__main__":
    main()
