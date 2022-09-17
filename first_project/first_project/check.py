import os


def check_files():

    path = "path"
    file_list = []

    for path, folders, files in os.walk(path):
        for file in files:
            file_list.append(os.path.join(path, file))

    return file_list


check_files()
