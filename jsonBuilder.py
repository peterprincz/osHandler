import string_handler
import sys_handler
from flask import jsonify


def drives_to_json(drives):
    result = {"driveList": drives}
    return jsonify(result)

def location_to_json(location):
    result = {"root_location": location}
    return jsonify(result)


def folders_to_json(list_of_folders):
    result = {"list_of_folders": list_of_folders}
    return jsonify(result)


def files_to_json(list_of_files):
    result = {"list_of_files": list_of_files}
    return jsonify(result)


def ip_to_json(ip_address):
    result = {'ip_address' : ip_address}
    return jsonify(result)


def detailed_files_to_json(list_of_files):
    for dict in list_of_files:
        dict["formatted_size"] = string_handler.humanbytes(dict["size"])
        dict["readable_modify_date"] = string_handler.humanTime(dict["modify_date"])
    return jsonify(list_of_files)


def butterfly_address(adress):
    result = {"ip_address": adress}
    return jsonify(result)
