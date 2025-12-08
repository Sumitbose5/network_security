'''
The setup.py file is an essential part of a Python project. It is used to provide metadata about the project and to define how the project should be built, packaged, and installed. This file typically includes information such as the project name, version, author, license, dependencies, and entry points.
'''

from setuptools import setup, find_packages
from typing import List

def get_requirements()->List[str]:
    """
    This function reads the requirements.txt file and returns a list of dependencies.
    """
    requirement_lst:List[str] = []
    try:
        with open("requirements.txt", "r") as file:
            #Read lines from the file
            lines=file.readlines()
            #Process each lines
            for line in lines:
                requirement = line.strip()
                #ignore empty lines and -e .
                if requirement and requirement != "-e .":
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found.")
        
    return requirement_lst


setup(
    name="NetworkSecurity",
    version="0.1.0",
    author="Sumit Bose",
    author_email="sumitkrbose05@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)