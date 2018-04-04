import os

def get_folder_dict(location):
    folder = dict()
    folder['folders'] = list()
    folder['files'] = list()
    for word in os.listdir(location):
        if os.path.isfile(location + "/" + word):
            folder['files'].append(word)
        else:
            if word[0] != '.':
                folder['folders'].append(word)
    return folder


def get_files_with_stat(location):
    files = get_folder_dict(location)['files']
    lista = list()
    for file in files:
        dicty = dict()
        dicty["name"] = file
        dicty["size"] = os.stat(location + "/" + file).st_size
        lista.append(dicty)
    return lista


def get_current_path():
    return os.getcwd()


def compress_folder(foldername, path):
    print("zipping   " + "zip -r " + "a" + ".zip " + path)
    os.system("zip -r " + foldername + ".zip . -i " + path)

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
