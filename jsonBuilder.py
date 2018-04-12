import sys_handler
from flask import jsonify


def location_to_json(location):
    result = {"root_location":location}
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