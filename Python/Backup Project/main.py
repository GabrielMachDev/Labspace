
import os
from tkinter.filedialog import askdirectory
import shutil
import datetime

selected_folder = askdirectory()

files_list = os.listdir(selected_folder)

# backup the files in this folder
backup_name = "backup"
complete_backup_name = f"{selected_folder}/{backup_name}"
if not os.path.exists(complete_backup_name):
    os.mkdir(complete_backup_name)

actual_date = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")

for file in files_list:
    complete_backup_name = f"{selected_folder}/{file}"
    final_backup_name = f"{complete_backup_name}/{actual_date}/{file}"
    
    if not os.path.exists(f"{complete_backup_name}/{actual_date}"):
        os.mkdir(f"{complete_backup_name}/{actual_date}")
    
    if "." in file:
        shutil.copy2(complete_backup_name, final_backup_name)
    elif "backup" != file:
        shutil.copytree(complete_backup_name, final_backup_name)
        