import my_utils
import os
import shutil

my_utils.say_hello()

os.mkdir("test_folder")
shutil.copy("file.txt", "test_folder ")

