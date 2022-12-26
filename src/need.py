import argparse
import os


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
    os.mkdir(project_name)

    # Print the project name and author name
    print(f'Created new project "{project_name}" by {author_name}')


def main():
    # Create a parser object
    parser = argparse.ArgumentParser()

    # Add a subcommand to the parser
    subcommands = parser.add_subparsers(dest='subcommand')

    # Create a parser for the "gen" subcommand
    gen_parser = subcommands.add_parser('gen')

    # Create a parser for the "new" subcommand
    new_parser = subcommands.add_parser('new')
    new_parser.add_argument('page_or_post', choices=['page', 'post'])
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
        new(args.page_or_post, args.name)
    elif args.subcommand == 'create':
        create(args.project_name, args.author_name)


if __name__ == '__main__':
    main()
