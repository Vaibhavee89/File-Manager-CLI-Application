# Core Filemanager functionalities: create, copy, move, delete, rename, list files.

import os
import shutil

try:
    from .persistence import save_data, load_data
    from .logger import log_action
except ImportError:
    # For direct script testing (not recommended for production)
    from persistence import save_data, load_data
    from logger import log_action

class FileManager:
    def __init__(self, base_path="data"):
        self.base_path = base_path
        os.makedirs(self.base_path, exist_ok=True)
        self.metadata = load_data()  # load existing data
    
    @log_action
    def create_file(self, filename, content=""):
        file_path = os.path.join(self.base_path, filename)
        if os.path.exists(file_path):
            return f"File '{filename}' already exists."
        with open(file_path, "w") as f:
            f.write(content)
        self.metadata[filename] = {"size": len(content)}
        save_data(self.metadata)
        return f"File '{filename}' created successfully."
    
    @log_action
    def read_file(self, filename):
        file_path = os.path.join(self.base_path, filename)
        if not os.path.exists(file_path):
            return f"File '{filename}' does not exist."
        with open(file_path, "r") as f:
            content = f.read()
        return content
    
    @log_action
    def update_file(self, filename, content):
        file_path = os.path.join(self.base_path, filename)
        if not os.path.exists(file_path):
            return f"File '{filename}' does not exist."
        with open(file_path, "w") as f:
            f.write(content)
        self.metadata[filename] = {"size": len(content)}
        save_data(self.metadata)
        return f"File '{filename}' updated successfully."
    
    @log_action
    def delete_file(self, filename):
        file_path = os.path.join(self.base_path, filename)
        if not os.path.exists(file_path):
            return f"File '{filename}' does not exist."
        os.remove(file_path)
        self.metadata.pop(filename, None)
        save_data(self.metadata)
        return f"File '{filename}' deleted successfully."
    
    @log_action
    def copy_file(self, src_filename, dest_filename):
        src_path = os.path.join(self.base_path, src_filename)
        dest_path = os.path.join(self.base_path, dest_filename)
        if not os.path.exists(src_path):
            return f"Source file '{src_filename}' does not exist."
        if os.path.exists(dest_path):
            return f"Destination file '{dest_filename}' already exists."
        shutil.copy2(src_path, dest_path)
        self.metadata[dest_filename] = {"size": os.path.getsize(dest_path)}
        save_data(self.metadata)
        return f"File '{src_filename}' copied to '{dest_filename}'."

    @log_action
    def move_file(self, src_filename, dest_filename):
        src_path = os.path.join(self.base_path, src_filename)
        dest_path = os.path.join(self.base_path, dest_filename)
        if not os.path.exists(src_path):
            return f"Source file '{src_filename}' does not exist."
        if os.path.exists(dest_path):
            return f"Destination file '{dest_filename}' already exists."
        shutil.move(src_path, dest_path)
        self.metadata[dest_filename] = self.metadata.pop(src_filename, {"size": os.path.getsize(dest_path)})
        save_data(self.metadata)
        return f"File '{src_filename}' moved to '{dest_filename}'."
    
    @log_action
    def rename_file(self, old_filename, new_filename):
        old_path = os.path.join(self.base_path, old_filename)
        new_path = os.path.join(self.base_path, new_filename)
        if not os.path.exists(old_path):
            return f"File '{old_filename}' does not exist."
        if os.path.exists(new_path):
            return f"File '{new_filename}' already exists."
        os.rename(old_path, new_path)
        self.metadata[new_filename] = self.metadata.pop(old_filename, {"size": os.path.getsize(new_path)})
        save_data(self.metadata)
        return f"File '{old_filename}' renamed to '{new_filename}'."

    @log_action
    def list_files(self):
        files = os.listdir(self.base_path)
        return [f for f in files if os.path.isfile(os.path.join(self.base_path, f))]

# For direct testing
if __name__ == "__main__":
    fm = FileManager()
    print(fm.list_files())
