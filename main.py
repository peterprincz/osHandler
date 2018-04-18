from werkzeug.utils import secure_filename

import jsonBuilder
import string_handler
import sys_handler
import random
from flask import Flask, render_template, redirect, request, session, jsonify, send_file, send_from_directory
import shutil
import os

app = Flask(__name__)


@app.route("/get_ip")
def get_up():
    ip_address = sys_handler.get_ip()
    return jsonBuilder.ip_to_json(ip_address)


@app.route("/")
def index():
    return app.send_static_file('templates/index2.html')


@app.route("/get_folders", methods=['POST'])
def get_folders():
    location = request.json['currentLocation']
    list_of_folders = sys_handler.get_folder_dict(location)['folders']
    return jsonBuilder.folders_to_json(list_of_folders)


@app.route("/get_files_with_size", methods=['POST'])
def get_files_with_size():
    location = request.json['currentLocation']
    list_of_file_dicts = sys_handler.get_files_with_stat(location)
    return jsonBuilder.detailed_files_to_json(list_of_file_dicts)


@app.route("/get_files", methods=['POST'])
def get_files():
    location = request.json['currentLocation']
    list_of_files = sys_handler.get_folder_dict(location)['files']
    return jsonBuilder.files_to_json(list_of_files)


@app.route("/get_root_path")
def get_location():
    path = sys_handler.get_current_path()
    return jsonBuilder.location_to_json(path)


@app.route("/download_file/<path>")
def download_file(path):
    real_path = string_handler.convert_parampath_to_realpath(path)
    folder_name = string_handler.get_folder_and_file(real_path)["folder_name"]
    file_name = string_handler.get_folder_and_file(real_path)["file_name"]
    try:
        return send_from_directory(folder_name, file_name, as_attachment=True)
    except Exception as e:
        print(e)


@app.route("/compress_folder/<path>")
def compress_folder(path):
    real_path = string_handler.convert_parampath_to_realpath(path)
    name_of_rar = string_handler.get_folder_name(real_path)
    return send_file(shutil.make_archive(name_of_rar, "zip", real_path), as_attachment=True)


@app.route('/upload_file/<path>', methods=['GET', 'POST'])
def upload_file(path):
    real_path = string_handler.convert_parampath_to_realpath(path)
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(real_path, filename))
            return 'OK', 200
    return 'Bad request', 300


if __name__ == "__main__":
    app.secret_key = "app_magic"
    msg = "The server is reachable on the :" + sys_handler.get_ip() + " address!"
    app.logger.critical(msg)
    app.run(
        host='0.0.0.0',
        debug=True,
        threaded=True,
        port=5000
    )


