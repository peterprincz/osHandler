import os
import operator


def get_folder_dict(location):
    base_folder = dict()
    base_folder['folders'] = list()
    base_folder['files'] = list()
    for word in os.listdir(location):
        if word[0] == '.':
            continue
        if os.path.isfile(location + "/" + word):
            base_folder['files'].append(word)
        else:
            base_folder['folders'].append(word)
    return base_folder


def get_files_with_stat(location):
    files = get_folder_dict(location)['files']
    list_of_file_dicts = list()
    for file in files:
        file_dict = dict()
        file_dict["name"] = file
        file_dict["size"] = os.stat(location + "/" + file).st_size
        list_of_file_dicts.append(file_dict)
    list_of_file_dicts.sort(key=operator.itemgetter("name"))
    return list_of_file_dicts


def get_current_path():
    return os.getcwd()


def move_back():
    current_path = get_current_path()
    if current_path != "/home":
        position_of_last_slash = -1
        for x in range(len(current_path) - 1, 0, -1):
            if current_path[x] == "/":
                position_of_last_slash = x
                break
        os.chdir(current_path[0:position_of_last_slash + 1])


def move_into_folder(subfolder):
    folder_to_move_into = get_current_path() + "/" + subfolder
    os.chdir(folder_to_move_into)
