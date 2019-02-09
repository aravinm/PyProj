import os

allowed_extensions = {".txt", ".csv", '.FOLDER'}

def folder_input():
    user_input_folder_path = raw_input("Enter the path of your folder:")
    if not os.path.isdir(user_input_folder_path):  # check for invalid folder path
        print "You have input an invalid folder path please try again"
    else:
        user_input_folder_path += '/'
        return user_input_folder_path
# end of error checking

