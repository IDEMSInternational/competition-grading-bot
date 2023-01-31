import subprocess


def setup_sdaps_project(tex_file, project_id):
    # TODO: Fill in code that sets up an SDAPS project for the given tex
    # file and with the given project id (=sdaps folder name).

    #The command for setting up sdaps project
    sdaps_command="sdaps setup folder_name",tex_file,"--add", images
    result = subprocess.run(sdaps_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
    
    #print the result
    print(result.stdout)

def parse_image(image, project_id):
    # Invokes SDAPS to process the image into a text format (e.g. csv).
    # Reads the output and prints it to the screen.
    
    # TODO: get the actual output and print it (student answers and other info).
    print("Student: Theo\nQ1: A\nA2: B\nQ3: D\nQ4: A")
