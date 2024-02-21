from setuptools import setup,find_packages
# from typing import List

# Declaring variables for the setup
PROJECT_NAME = 'housing-predictor'
VERSION = '0.0.3'
AUTHOR = 'Sparsha Srinath'
DESCRIPTION = 'Predicting the price of houses in the US'
REQUIREMENTS_FILE_NAME = 'requirements.txt'

def get_requirements_list() :
    """
    Description: This function reads the requirements.txt file and returns a list of requirements
    return: This function returns a list of libraries that are in the requirements.txt file
    """
    with open(REQUIREMENTS_FILE_NAME) as file:
        return file.readlines()



setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=   AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list()
)

