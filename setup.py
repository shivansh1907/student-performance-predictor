from setuptools import setup, find_packages

from typing import List

def get_requiremnts(file_path)->List[str]:
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if "-e ." in requirements:
            requirements.remove("-e .")
    return requirements

setup(
    name="my_package",
    version="0.0.1",
    packages=find_packages(),   
    author="shivansh",
    install_requires=get_requiremnts("requirements.txt")
)