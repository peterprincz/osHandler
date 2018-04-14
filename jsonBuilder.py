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


def detailed_files_to_json(list_of_files):
    for dict in list_of_files:
        dict["formatted_size"] = humanbytes(dict["size"])
    return jsonify(list_of_files)


def humanbytes(B):
    B = float(B)
    KB = float(1024)
    MB = float(KB ** 2) # 1,048,576
    GB = float(KB ** 3) # 1,073,741,824
    TB = float(KB ** 4) # 1,099,511,627,776

    if B < KB:
        return '{0} {1}'.format(B,'Bytes' if 0 == B > 1 else 'Byte')
    elif KB <= B < MB:
        return '{0:.2f} KB'.format(B/KB)
    elif MB <= B < GB:
        return '{0:.2f} MB'.format(B/MB)
    elif GB <= B < TB:
        return '{0:.2f} GB'.format(B/GB)
    elif TB <= B:
        return '{0:.2f} TB'.format(B/TB)