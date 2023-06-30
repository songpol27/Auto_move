import os, shutil
from configparser import ConfigParser

#Get config form config.ini
config = ConfigParser()
config.read('config.ini')
source_folder =  config.get('Folder', 'source_folder')
destination_folder = config.get('Folder', 'destination_folder')
print(f"Source : {source_folder} \nDestination : {destination_folder}")


