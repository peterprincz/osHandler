import os
import operator
import socket
from pathlib import Path

import string_handler

import win32api

#for windows
def get_drives():
    drives = win32api.GetLogicalDriveStrings()
    drives = drives.split('\000')[:-1]
    return drives


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
        file_dict["modify_date"] = os.stat(location + "/" + file).st_mtime
        list_of_file_dicts.append(file_dict)
    list_of_file_dicts.sort(key=operator.itemgetter("name"))
    return list_of_file_dicts


def get_current_path():
    #return os.getcwd()
    return str(Path.home())


def move_back():
    current_path = get_current_path()
    next_path = string_handler.move_back(current_path)
    os.chdir(next_path)


def move_into_folder(subfolder):
    folder_to_move_into = get_current_path() + "/" + subfolder
    os.chdir(folder_to_move_into)


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("10.255.255.255", 1))
        IP = s.getsockname()[0]
    except:
        IP = "127.0.0.1"
    finally:
        s.close()
    return IP



def launch_butterfly():
    os.system("butterfly.server.py --host="+get_ip()+" --port=57575 --unsecure")
