from setuptools import setup
from typing import List

def get_requirements_list() -> List[str]:
    """
    Description: This function reads the requirements.txt file and returns a list of requirements
    return: This function returns a list of libraries that are in the requirements.txt file
    """
    with open(REQUIREMENTS_FILE_NAME) as file:
        return file.readlines()
# Declaring variables for the setup
PROJECT_NAME = 'housing-predictor'
VERSION = '0.0.1'
AUTHOR = 'Sparsha Srinath'
DESCRIPTION = 'Predicting the price of houses in the US'
PACKAGES = ['housing']
REQUIREMENTS_FILE_NAME = 'requirements.txt'
setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=   AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGES,
    install_requires=get_requirements_list()
)

