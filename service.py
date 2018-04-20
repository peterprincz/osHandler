import shutil

from werkzeug.utils import secure_filename

import jsonBuilder
import string_handler
import sys_handler
import os


def get_ip():
    ip_address = sys_handler.get_ip()
    return jsonBuilder.ip_to_json(ip_address)


def get_folders(request):
    location = request.json['currentLocation']
    list_of_folders = sys_handler.get_folder_dict(location)['folders']
    return jsonBuilder.folders_to_json(list_of_folders)


def get_files_with_size(request):
    location = request.json['currentLocation']
    list_of_file_dicts = sys_handler.get_files_with_stat(location)
    return jsonBuilder.detailed_files_to_json(list_of_file_dicts)


def get_files(request):
    location = request.json['currentLocation']
    list_of_files = sys_handler.get_folder_dict(location)['files']
    return jsonBuilder.files_to_json(list_of_files)


def get_location():
    path = sys_handler.get_current_path()
    return jsonBuilder.location_to_json(path)


def get_file_for_download(path):
    real_path = string_handler.convert_parampath_to_realpath(path)
    folder_name = string_handler.get_folder_and_file(real_path)["folder_name"]
    file_name = string_handler.get_folder_and_file(real_path)["file_name"]
    return {"folder_name": folder_name, "file_name" : file_name}


def make_rar_for_download(path):
    real_path = string_handler.convert_parampath_to_realpath(path)
    name_of_rar = string_handler.get_folder_name(real_path)
    return shutil.make_archive(name_of_rar, "zip", real_path)


def save_file(file, path):
    real_path = string_handler.convert_parampath_to_realpath(path)
    filename = secure_filename(file.filename)
    file.save(os.path.join(real_path, filename))
