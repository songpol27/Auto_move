import os
import shutil
import datetime
from configparser import ConfigParser

#Check the conditions whether the specified date has been exceeded or not.
def check_date_diff(input_date, Date_condition_move):
    Bool_result = False
    input_date = datetime.datetime.strptime(input_date, "%Y%m%d").date()
    current_date = datetime.datetime.now().strftime("%Y%m%d")
    current_date = datetime.datetime.strptime(current_date, "%Y%m%d").date()
    difference = (current_date - input_date).days
    if difference > Date_condition_move:
        Bool_result = True
    else:
        Bool_result = False

    return Bool_result

# Move file
def move_folder(source_folder, destination_folder, input_date, Date_condition_move):
    Statue = check_date_diff(input_date, Date_condition_move) #call method Check the conditions whether the specified date has been exceeded or not.
    if Statue :
        New_source_path = source_folder + "\\" + str(input_date)
        try:
            shutil.move(New_source_path, destination_folder)
            New_path = destination_folder + "\\" + str(input_date)
            separate_folder(New_path)
            print(f"Folder moved successfully from {New_source_path} to {destination_folder}.")
        except Exception as e:
            print(f"An error occurred while moving the folder: {e}")
    else: 
        print("No condition matching to move file")



def create_folder(folder_path):
    try:
        os.makedirs(folder_path)
        print(f"Folder created successfully at {folder_path}.")
    except Exception as e:
        print(f"An error occurred while creating the folder: {e}")

def separate_folder(path_folders):
    path_folder = os.listdir(path_folders)
    for folder in path_folder:
        folder = path_folders + "\\" + folder 

        Name_items = os.listdir(folder)
        
        for item in Name_items:
            try:
                source_path = folder + "\\" + item
                Statue_Pic= item.split("_")[1]
                OCR_code = item.split("_")[4].split(".")[0]
                Destination_folder = folder + "\\" + Statue_Pic + "\\" + OCR_code
                Destination_path = folder + "\\" + Statue_Pic + "\\" + OCR_code +"\\"+ item

                print(f"Source : {source_path} Statue : {Statue_Pic} OCR code : {OCR_code} Destination : {Destination_path}")
                try:
                    shutil.move(source_path, Destination_path)
                except:   
                    create_folder(Destination_folder)
                    shutil.move(source_path, Destination_path)
            except Exception as e:
                pass

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
            move_folder(source_folder, destination_folder, folder, 2)
    else:
        print("The source_folder does not contain any folders.")

if __name__ == "__main__":
    #main()
    separate_folder(r"C:\Users\1000267027\Desktop\move\Distination")
