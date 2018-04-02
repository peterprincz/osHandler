import os

def get_current_folder():
    folder = dict()
    folder['folders'] = list()
    folder['files'] = list()
    for word in os.listdir():
        if(word[0] != '.'):
            if '.' in word:
                folder['files'].append(word)
            else:
                folder['folders'].append(word)
    return folder


def get_current_path():
    return os.getcwd()


def compress_folder(foldername):
    print("zipping   " + "zip -r " + foldername + ".zip " + foldername)
    os.system("zip -r " + foldername + ".zip . -i " + foldername)


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
