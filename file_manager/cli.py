# This would be the main entry point for the CLI application

import argparse
try:
    from .manager import FileManager
except ImportError:
    from manager import FileManager

def main():
    fm = FileManager() # Initialize the FileManager

    parser = argparse.ArgumentParser(description="File Manager CLI") # Create the top-level parser

    subparsers = parser.add_subparsers(dest="command", help="Available commands") # Create subparsers for each command

    # Create file
    create_parser = subparsers.add_parser("create", help="Create a new file")
    create_parser.add_argument("filename", help="Name of the file to create")
    create_parser.add_argument("--content", default="", help="Content of the file")

    # Read file
    read_parser = subparsers.add_parser("read", help="Read a file")
    read_parser.add_argument("filename", help="Name of the file to read")

    # Update file
    update_parser = subparsers.add_parser("update", help="Update a file")
    update_parser.add_argument("filename", help="Name of the file to update")
    update_parser.add_argument("content", help="New content for the file")

    # Delete file
    delete_parser = subparsers.add_parser("delete", help="Delete a file")
    delete_parser.add_argument("filename", help="Name of the file to delete")

    # List files
    subparsers.add_parser("list", help="List all files")

    args = parser.parse_args()

    # Handle commands
    if args.command == "create":
        print(fm.create_file(args.filename, args.content))
    elif args.command == "read":
        print(fm.read_file(args.filename))
    elif args.command == "update":
        print(fm.update_file(args.filename, args.content))
    elif args.command == "delete":
        print(fm.delete_file(args.filename))
    elif args.command == "list":
        print(fm.list_files())
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
