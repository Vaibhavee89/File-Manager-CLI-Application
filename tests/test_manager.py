import os
import pytest
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from file_manager.manager import FileManager
from file_manager.persistence import load_data

TEST_DIR = "test_data"

@pytest.fixture
def fm():
    # setup
    fm = FileManager(base_path=TEST_DIR)
    yield fm
    # teardown (cleanup after tests)
    for f in os.listdir(TEST_DIR):
        os.remove(os.path.join(TEST_DIR, f))
    os.rmdir(TEST_DIR)

def test_create_file(fm):
    result = fm.create_file("test.txt", "Hello Test")
    assert "created successfully" in result
    assert os.path.exists(os.path.join(TEST_DIR, "test.txt"))

def test_read_file(fm):
    fm.create_file("test.txt", "Read Me")
    content = fm.read_file("test.txt")
    assert content == "Read Me"

def test_update_file(fm):
    fm.create_file("test.txt", "Old Content")
    result = fm.update_file("test.txt", "New Content")
    assert "updated successfully" in result
    content = fm.read_file("test.txt")
    assert content == "New Content"

def test_delete_file(fm):
    fm.create_file("test.txt", "To Delete")
    result = fm.delete_file("test.txt")
    assert "deleted successfully" in result
    assert not os.path.exists(os.path.join(TEST_DIR, "test.txt"))

def test_list_files(fm):
    fm.create_file("a.txt", "A")
    fm.create_file("b.txt", "B")
    files = fm.list_files()
    assert "a.txt" in files and "b.txt" in files

def test_persistence(fm):
    fm.create_file("persist.txt", "Keep Me")
    metadata = load_data()
    assert "persist.txt" in metadata
