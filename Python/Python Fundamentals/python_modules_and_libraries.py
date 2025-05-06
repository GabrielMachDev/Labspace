import os
# import datetime
# import pyautogui

# pyautogui.press("win")
# pyautogui.write("chrome")

# print(os.listdir("files"))
# print(datetime.date.today())

files_list = os.listdir("files")
# os.rename("files/abr22.txt", "files/22/abr22.txt")

for file in files_list:
    if ".txt" in file:
        if "22" in file:
            os.rename(f"files/{file}", f"files/22/{file}")
        elif "23" in file:
            os.rename(f"files/{file}", f"files/23/{file}")