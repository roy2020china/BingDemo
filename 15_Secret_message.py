# There are images for "A~Z", " " and "," in file folder named "alphabet", which can be downloaded from https://s3.amazonaws.com/udacity-hosted-downloads/ud036/alphabet.zip . Images are downloaded and stored on my local machine at "/Users/ABC/Temp/alphabet/". 
# Prompt user to provide a name for a new file folder, such as "test_folder". File path is "/Users/ABC/Temp/test_folder/"
# Prompt user to provide a hidden message, such as "love you python".
# Pick photos from alphabet according to the user's hidden message and move them to test_folder. In our case, chennai.jpg, dallas1.jpg, ithaca.jpg, beijing.jpg, madrid1.jpg, kiev1.jpg, dallas2.jpg, istanbul.jpg, madrid2.jpg, delhi.jpg, kiev2.jpg, hyderabad.jpg, bristol.jpg, dallas3.jpg, colombo.jpg will be selected and moved to test_folder.
# Re-arrange all the photos in test_folder in the order of "LOVE YOU PYTHON".


import os
import string
import shutil  # copy one file from Folder A to Folder B; or copy one file folder recursively to Folder B

# Step 1.1: prompt user to input a folder name. create a folder.
def user_input_folder_name():
    folder_name = raw_input("Please give a name for the folder to be created:")
    print "Got the folder name. Thank you."
    return folder_name

def create_folder():
    folder_name = user_input_folder_name()
    while os.path.exists("/Users/ABC/Temp/" + folder_name) is True:
        print "Please give a valid name"
        folder_name = user_input_folder_name()
    # create a folder with that name
    folder_path = "/Users/ABC/Temp/" + folder_name
    print "folder path is: " + folder_path
    # os.makedirs("/Users/ABC/Temp/%s" % folder_name)
    os.makedirs(folder_path)
    return folder_path


# Step 1.2: prompt user to create a hidden message, rename those photo files which are used for more than once. Move those photo files into it
def user_input_hidden_message():
    hidden_message = raw_input("the hidden message that you want to print out after implementation of this program: ")
    hidden_message = hidden_message.upper()
    return hidden_message


# a ~ z, plus . and blank space.
def get_alphabet_list():
    # get a string of "a~z", or "A~Z", or "a~zA~Z"
    # alphabet = string.ascii_letters
    alphabet = string.ascii_uppercase
    # make a list
    alphabet_list = list(alphabet)
    return alphabet_list


# Step 1.3: make a dictionary, key = "A~Z", value = file_name
def file_names_list():
    cwd = "/Users/ABC/Temp/alphabet"
    file_names = os.listdir(cwd)
    # remove ".DS_Store" from the list
    file_names.pop(0)
    return file_names


def dict_alphabet_filename():
    keys = get_alphabet_list()
    values = file_names_list()
    return dict(zip(keys, values))


def dict_28_keyvaluepairs():
    # dict_28 = {" ":"madrid.jpg", ".": "los angles.jpg"}
    dict_28 = dict_alphabet_filename()
    dict_28[" "] = "madrid.jpg"
    dict_28["."] = "los angles.jpg"
    return dict_28


# Step 1.4: select photo files according to the hidden message, rename it if it is used for more than once, move them to the folder.
def select_files_according_to_hidden_message(folder_path, hidden_message):
    #folder_path = create_folder()
    #hidden_message = user_input_hidden_message()

    # make a list based on the string of hidden_message
    hidden_message_list = list(hidden_message)

    # get all keys from dict_28
    dict_28 = dict_28_keyvaluepairs()

    # get_all_keys = dict.keys()
    hidden_message_file_names = []
    i = 0
    # print "dict_28['l']: " + dict_28["l"]
    # print "dict_28:"
    # print dict_28
    for each_item in hidden_message_list:
        file_name = dict_28[each_item]
        # if file_name in hidden_message_file_names is not True: -- WRONG
        if file_name not in hidden_message_file_names:
            hidden_message_file_names.append(file_name)
            shutil.copy(("/Users/ABC/Temp/alphabet/" + file_name), folder_path)
        else:
            # modify the file name before append() it to the hidden_message_file_names list
            file_name_index = file_name[:-4] + str(i) + file_name[-4:]
            hidden_message_file_names.append(file_name_index)
            # copy the file under the name of file_name and paste as file_name_index
            shutil.copy(("/Users/ABC/Temp/alphabet/" + file_name), (folder_path+ "/" + file_name_index))
        i += 1
    return hidden_message_file_names


# Step 2: rename all files so that they will be displayed in the desired order, which in our case is "LOVE YOU PYTHON"
def rearrange_files_according_to_hidden_message(folder_path, hidden_message):
    # create a folder under the name provided by the user, in our case test_folder. Select photos, copy and paste them to test_folder
    file_names = select_files_according_to_hidden_message(folder_path, hidden_message)

    # copy test_folder recursively and paste it as test_folder_copy
    # cwd = os.getcwd()
    # print "current working directory cwd is: " + cwd
    # os.chdir("/Users/ABC/Temp")
    # cwd1 = os.getcwd()
    # print "current working directory cwd1 is: " + cwd1
    copy_folder_path = folder_path + "_copy"

    # change working directory to copy_folder_path's parent
    os.chdir("/Users/ABC/Temp")
    # cwd = os.getcwd()
    # print "current working directory cwd is: " + cwd
    shutil.copytree(folder_path, copy_folder_path)

    # change working directory to copy_folder_path
    os.chdir(copy_folder_path)

    # rename all the file in test_folder_copy so that they will show "LOVE YOU PYTHON"
    i = 0
    for file_name in file_names:
        # rename each file to a new name in the pattern of index + file_name
        new_file_name = str(i) + file_name
        os.rename(file_name, new_file_name)
        i += 1

# Step 3: remove numbers from file names, in order to show the hidden message.


def main():
    os.chdir('/Users/ABC/Temp')
    #user_input_folder_name()
    folder_path = create_folder()
    hidden_message = user_input_hidden_message()
    #get_alphabet_list()
    #file_names_list()
    #dict_alphabet_filename()
    #select_files_according_to_hidden_message(folder_path, hidden_message)
    rearrange_files_according_to_hidden_message(folder_path, hidden_message)


main()
