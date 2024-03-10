import yaml 
from housing.exception import HousingException
import os,sys

def read_yaml_file(config_path:str)->dict:
    """
    Read the yaml file and return the dictionary
    file_path: str : path of the yaml file
    return : dict : dictionary of the yaml file
    """
    
    try:
        with open(config_path, 'rb') as yaml_file: 
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException(e,sys) from e