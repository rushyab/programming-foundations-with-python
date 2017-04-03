import os
from string import digits

def rename_files():

    #(1) get file names from the folder
    file_list = os.listdir(r"E:\programming-foundations-with-python\1-use_functions\prank")
    # print(file_list)
    saved_path = os.getcwd() # save the current path before changing it
    print("current working Directorty is: "+saved_path)
    os.chdir(r"E:\programming-foundations-with-python\1-use_functions\prank")

    #(2) for each file, rename filename
    for file_name in file_list:
        remove_digits = str.maketrans('', '', digits)
        new_file_name = file_name.translate(remove_digits)
        print("Old name - {}".format(file_name))
        print("New name - {}".format(new_file_name))
        os.rename(file_name, new_file_name)
    os.chdir(saved_path)

    
rename_files()
