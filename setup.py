from setuptools import setup, find_packages

setup(
    name="file_manager",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "filemanager=file_manager.cli:main",
        ],
    },
)
