import os
import random
import shutil

"""This is a collection of basic function to work with the folders"""

#Get the names of directories from a path to its parent directory
def get_dir_names(main_path):
    folder_files_count = []
    for folder in os.listdir(main_path):
        if os.path.isdir(os.path.join(main_path, folder)):
            folder_files_count.append(folder)
    return folder_files_count

#Get the number of files from a directory
def get_dir_file_count(main_path):
    count = 0
    for path in os.listdir(main_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(main_path, path)):
            count += 1
    return count

#Create a path given a parent path and a directory name
def get_path(main_path, dir_name):
    return main_path + "\\" + dir_name

#Take a number of random images from the source path and move them to the destination path directory
def random_file_fetcher(source_path, dest_path, files_to_move):
    for i in range(files_to_move):
        random_file = random.choice(os.listdir(source_path))

        source_file = "%s\\%s" % (source_path, random_file)
        print(source_file,random_file)
        shutil.move(source_file, dest_path)


def rename_all_files_to_numbers(source_path, concat_string=""):
    counter_image_name = 0
    for file in os.listdir(source_path):
        if os.path.isfile(os.path.join(source_path, file)):
            os.rename(get_path(source_path,file), get_path(source_path, str(concat_string)
                                                           + str(counter_image_name)+".jpg"))
            counter_image_name += 1

