import argparse
import os
import markdown
import shutil
import datetime
from need_templater import templater



def gen():
    # Generate
    print('Test')


def new(extension, name):
    if not (extension in ['page', 'post']):
        raise ValueError('Invalid option: must be "page" or "post"')
    # Create a new file called "name.page.nd" or "name.post.nd"
    with open(f'{name}.{extension}.nd', 'w') as f:
        f.write('')


def create(project_name, author_name):
    # Create a new directory with the given project name
    try:
        os.mkdir(project_name)
    except:
        print("An error has occurred while creating the project")
        return
    # Status Update
    print("Created Directory: " + project_name)
    print("Populating Directory...")
    # Get the file path of the script
    # Get the file path of the script
    script_src_path = os.path.dirname(os.path.abspath(__file__))

    templates_dir_path = os.path.join(script_src_path, "templates")

    up_dir_path = os.path.join("..", script_src_path)

    config_path = os.path.join(templates_dir_path, "config.yaml")

    license_path = os.path.join(templates_dir_path, "LICENSE")

    readme_path = os.path.join(templates_dir_path, "README.md")
    
    project_path = os.path.join(os.getcwd(), project_name)
    print(up_dir_path)
    # Populate directory with template files
    # config.yaml
    shutil.copy(config_path, project_path)
    # sources directory
    os.mkdir(project_name+"/sources")
    # license
    license_map = {'{{author_name}}': author_name, '{{year}}': str(datetime.datetime.utcnow().year)}
    for k in license_map.keys():
        print(k)
    templater(license_path, license_map, os.path.join(project_path, "LICENSE"))
    # readme
    shutil.copy(readme_path, project_path)


    print("Finished! Project Created")
    return


def main():
    # Create a parser object
    parser = argparse.ArgumentParser()
    # Add a subcommand to the parser
    subcommands = parser.add_subparsers(dest='subcommand')
    # Create a parser for the "gen" command
    _ = subcommands.add_parser('gen')
    # Create a parser for the "new" subcommand
    new_parser = subcommands.add_parser('new')
    new_parser.add_argument('extension', choices=['page', 'post'])
    new_parser.add_argument('name')
    # Create a parser for the "create" subcommand
    create_parser = subcommands.add_parser('create')
    create_parser.add_argument('project_name')
    create_parser.add_argument('author_name')
    # Parse the arguments
    args = parser.parse_args()
    # Call the appropriate function based on the subcommand
    if args.subcommand == 'gen':
        gen()
    elif args.subcommand == 'new':
        new(args.extension, args.name)
    elif args.subcommand == 'create':
        create(args.project_name, args.author_name)


if __name__ == '__main__':
    main()
