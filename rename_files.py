import os

def rename_files():
    file_list = os.listdir('/Users/Federico/Desktop/python-course/rename_test_folder')
    os.chdir('/Users/Federico/Desktop/python-course/rename_test_folder');
    for file_name in file_list:
        new_file_name = file_name.translate(None, "0123456789")
        print('Renaming ' + file_name + ' to ' + new_file_name)
        os.rename(file_name, new_file_name)
rename_files()
