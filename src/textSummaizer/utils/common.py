import os
from box.exceptions import BoxValueError
import yaml
from textSummaizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any 


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file and returns its content as a ConfigBox object.
    
    Args:
        path_to_yaml (Path): Path to the YAML file.
        
    Returns:
        ConfigBox: Content of the YAML file as a ConfigBox object.
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file {path_to_yaml} read successfully.")
            return ConfigBox(content)
    except FileNotFoundError as e:
        logger.error(f"YAML file not found: {e}")
        raise ValueError("YAML file not found. Please check the path.")
    
    except BoxValueError as e:
        logger.error(f"Error in YAML content: {e}")
        raise e
    
    
@ensure_annotations
def create_directories(paths: list, verbose=True):
    """
    Creates directories if they do not exist.
    
    Args:
        paths (list[Path]): List of directory paths to create.
    """
    for path in paths:
       os.makedirs(path, exist_ok=True)
       if verbose:
           logger.info(f"Created directory: {path}")    
        
@ensure_annotations
def get_file_size(file_path: Path) -> int:
    size_in_kb=round(os.path.getsize(file_path) / 1024)
    return f"{size_in_kb} KB"