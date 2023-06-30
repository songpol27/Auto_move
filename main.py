import os
import shutil
import datetime
from configparser import ConfigParser

def main():
    # Get config from config.ini
    config = ConfigParser()
    config.read('config.ini')
    source_folder = config.get('Folder', 'source_folder')
    destination_folder = config.get('Folder', 'destination_folder')
    print(f"Source: {source_folder}\nDestination: {destination_folder}")

    # Check if source_folder contains any folders
    folders = [item for item in os.listdir(source_folder) if os.path.isdir(os.path.join(source_folder, item))]
    if folders:
        print("The source_folder contains the following folders:")
        for folder in folders:
            date_folder = datetime.datetime.strptime(folder, "%Y%m%d").date()
            print(date_folder)
    else:
        print("The source_folder does not contain any folders.")

if __name__ == "__main__":
    main()
