import os
from box.exceptions import BoxValueError
import yaml
from textClassifier.logging import logger

from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import AnyStr

@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    """read yaml files and return

    Args: 
        path_to_yaml(str): path like input
    Raises: 
        ValueError: if yaml file is empty
    Return: 
        ConfigBox: ConfigBox:Type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yamlfile: {path_to_yaml} lodded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("Yaml file is empty")
    except Exception as e:
        raise 

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Create a list of Directories
    Args: 
        path_to_directories(list): list of path direcotires
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose: 
            logger.info(f"Created Directory at: {path}")

@ensure_annotations
def get_size(path:Path) -> str:
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"