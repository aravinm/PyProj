import re
import os
import glob

allowed_extensions = {".txt", ".csv", '.FOLDER'}

while True:
    user_input_folder_path = raw_input("Enter the path of your folder:")
    if not os.path.isdir(user_input_folder_path):  # check for invalid folder path
        print "You have input an invalid folder path please try again"
        continue
    else:
        flag = None
        num = 5
        for files in os.listdir(user_input_folder_path):  # check if all files in directory are .txt or .csv extension
            extension = os.path.splitext(files)[1]
            if extension not in allowed_extensions:
                print "Your folder can only contain .txt and .csv files, please try again"
                flag = False
            else:
                flag = True

        if flag == False:
            continue
        else:
            break
# end of error checking


# Start of loop to look for txt files and their file names in folder
required_extensions = {".txt"}

for filename in os.listdir(user_input_folder_path):
    extension = os.path.splitext(filename)[1]
    if extension in required_extensions:
        print filename
    else:
        pass
