# File Manager CLI Application

A simple, modular command-line application to manage files and directories.  
Supports creating, reading, updating, deleting, copying, moving, renaming, and listing files.  
All actions are logged and file metadata is persisted for easy tracking.

---

## Features

- **Create** files with custom content
- **Read** file contents
- **Update** file contents
- **Delete** files
- **Copy** files
- **Move** files
- **Rename** files
- **List** all files in the managed directory
- **Action Logging**: Every operation is logged for auditing
- **Metadata Persistence**: File sizes and names are tracked

---

## Getting Started

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/file-manager-cli.git
cd file-manager-cli
```

### 2. Install Dependencies

This project uses only Python’s standard library.  
No extra dependencies are required.

### 3. Project Structure

```
file-manager-cli/
├── data/                # Stores files, logs, and metadata
├── file_manager/        # Source code
│   ├── manager.py
│   ├── logger.py
│   ├── persistence.py
│   ├── cli.py
│   └── __init__.py
├── tests/               # Unit tests
│   └── test_manager.py
├── README.md
└── setup.py
```

---

## Usage

### Run the CLI

From the project root, use the following commands:

#### Create a File

```sh
python -m file_manager.cli create myfile.txt --content "Hello, World!"
```

#### Read a File

```sh
python -m file_manager.cli read myfile.txt
```

#### Update a File

```sh
python -m file_manager.cli update myfile.txt --content "New content"
```

#### Delete a File

```sh
python -m file_manager.cli delete myfile.txt
```

#### Copy a File

```sh
python -m file_manager.cli copy myfile.txt copy.txt
```

#### Move a File

```sh
python -m file_manager.cli move copy.txt moved.txt
```

#### Rename a File

```sh
python -m file_manager.cli rename moved.txt renamed.txt
```

#### List All Files

```sh
python -m file_manager.cli list
```

---

## Logging & Metadata

- **Logs:** All actions are recorded in `data/actions.log`.
- **Metadata:** File information is stored in `data/files.json`.

---

## Testing

Unit tests are provided using `pytest`.

### Run All Tests

```sh
pytest
```

Tests are located in the `tests/` directory and cover all major functionalities.

---

## Notes

- Always run commands from the project root for correct file paths.
- The application uses the `data/` directory for all file operations by default.
- All actions are logged for traceability.

---

## License

MIT License

---

## Author

Your Name