import sys_handler
from flask import jsonify

def get_location():
    result = {"current_location" : sys_handler.get_current_path()}
    return jsonify(result)


def get_folders():
    list_of_folders = sys_handler.get_current_folder()['folders']
    result = {"list_of_folders": list_of_folders}
    return jsonify(result)


def get_files():
    list_of_files = sys_handler.get_current_folder()['files']
    result = {"list_of_files" : list_of_files}
    return jsonify(result)
