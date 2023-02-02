import subprocess
import csv

def setup_sdaps_project(tex_file,project_id):
    # TODO: Fill in code that sets up an SDAPS project for the given tex
    # file and with the given project id (=sdaps folder name).

    #The command for setting up sdaps project
    create_project_command=['sdaps','setup', './assets/results/folder_name'+project_id,tex_file,'--add','./coins']
    subprocess.run(create_project_command)

    return 'folder_name'+project_id
    

def parse_image(image,project_id):
    # Invokes SDAPS to process the image into a text format (e.g. csv).
    # Reads the output and prints it to the screen.

     # Calling setup for folder

    folder_name = setup_sdaps_project("./assets/example.tex",project_id)
    print(folder_name, 'is the following here!')

    # accepting the scanned image
    scanned_images_command=['sdaps', 'add', './assets/results/folder_name'+project_id,'--convert',image]
    subprocess.run(scanned_images_command)

    #Run Optical mark recognition
    recoginize_image_command=['sdaps','recognize','./assets/results/'+folder_name]
    subprocess.run(recoginize_image_command)

    # # reporting csv result
    changing_csv_report=['sdaps','csv','export','./assets/results/'+folder_name]
    subprocess.run(changing_csv_report)
    
    # TODO: get the actual output and print it (student answers and other info).
    # print("Student: Theo\nQ1: A\nA2: B\nQ3: D\nQ4: A")
    with open('./assets/results/folder_name'+project_id+'/data_1.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# setup_sdaps_project("./assets/example.tex",'005')
parse_image("./assets/example-scan.pdf",'003')
