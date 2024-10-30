from dir_functions import *
from os import listdir
"""
    The dataset I choose is unbalance, because more than 95% of the images are in the training data folder,
    that´s why this code exits. Its main function is to take random images from the training collection and move them
    to the validation and test collections, to have the required percentages of data in each folder (70% training,
    20% validation, 10% test)
"""
main_dir_path = r'C:\Users\yabpe\Documents\VC\P4\dataset'

#Get the names where the 3 parts of the dataset exists
dir_main_dir_names = get_dir_names(main_dir_path)
#Get the name of the training folder
source_dir_path = get_path(main_dir_path, dir_main_dir_names[1])
valid_dir_path = get_path(main_dir_path, dir_main_dir_names[2])
test_dir_path = get_path(main_dir_path, dir_main_dir_names[0])

dir_count_files = get_dir_file_count(source_dir_path)
dir_aprox_count_files_validation = round(dir_count_files*20/100)
dir_aprox_count_files_test = round(dir_count_files10*/100)


random_file_fetcher(source_dir_path, valid_dir_path,dir_aprox_count_files_validation)
random_file_fetcher(source_dir_path, test_dir_path,dir_aprox_count_files_test)



print(dir_count_files-dir_aprox_count_files_validation-dir_aprox_count_files_test)
print(dir_aprox_count_files_validation)
print(dir_aprox_count_files_test)


