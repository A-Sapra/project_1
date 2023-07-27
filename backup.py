from data import log_to_db

import shutil
import os
import datetime

# getting backup folder path from the environment variable
backup_folder_path = os.environ.get('BACKUPFOLDER')
if backup_folder_path is None or not backup_folder_path:
    backup_folder_path = './backup'

# this creates a backup folder if one does not exist already
if not os.path.exists(backup_folder_path):
    os.makedirs(backup_folder_path)


# defines function to backup folder
def backup_folder(source_folder_path):
    if not os.path.exists(source_folder_path):
        log_to_db("BACKUP", "Folder=" + source_folder_path, "ERROR")
        raise ValueError("Source folder does not exist")

    # This creates the timestamp for the backup folder name
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    backup_folder_name = f"{os.path.basename(source_folder_path)}_{timestamp}"
    backup_path = os.path.join(backup_folder_path, backup_folder_name)

    # copy the contents of the source folder into the backup folder
    shutil.copytree(source_folder_path, backup_path)

    log_to_db("BACKUP", "Folder=" + source_folder_path, "SUCCESS")


#def backup_file(source_file_path):
#    if not os.path.exists(source_file_path):
#        log_to_db("BACKUP", "File=" + source_file_path, "ERROR")
#        raise ValueError("Source file does not exist")

    # This creates the timestamp for the backup file name
#    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
#    backup_file_name = f"{os.path.basename(source_file_path)}_{timestamp}"
#    backup_path = os.path.join(backup_folder_path, backup_file_name)

    # copy the contents of the source folder
#    shutil.copytree(source_file_path, backup_path)
#
#    log_to_db("BACKUP", "File=" + source_file_path, "SUCCESS")
