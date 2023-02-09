import argparse
from sdaps_tools import setup_sdaps_project, delete_sdaps_project, parse_image


def main():
    description = 'Write something here.\n\n'
    parser = argparse.ArgumentParser(description=description, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('command', 
            choices=["setup_project", "parse_image", "delete_project"],
            help='Some text here.\n')
    parser.add_argument('project_id', help='ID/name of the project')
    parser.add_argument('input', nargs='?', help='Filename of the .tex file or scan image')
    parser.add_argument('--image_folder', help='Folder with images referenced by the .tex.')
    args = parser.parse_args()

    if args.command == 'setup_project':
        if not args.input:
            print("input parameter required")
            return
        setup_sdaps_project(args.input, args.project_id, args.image_folder)
    elif args.command == 'delete_project':
        delete_sdaps_project(args.project_id)
    elif args.command == 'parse_image':
        if not args.input:
            print("input parameter required")
            return
        result = parse_image(args.input, args.project_id)
        for k,v in result.items():
            if v != '':
                print(f"{k}: {v}")


if __name__ == "__main__":
    main()
