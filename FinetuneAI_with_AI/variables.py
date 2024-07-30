import os

base_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the absolute path to the resource file
resource_file_path = os.path.join(base_dir, 'resources', 'DatasetPreProcessor.py')
CODE_OUPUT_PATH:str=resource_file_path