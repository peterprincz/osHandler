import jsonBuilder
import sys_handler
import random
from flask import Flask, render_template, redirect, request, session, jsonify, send_file, send_from_directory
import shutil
import socket

app = Flask(__name__)
current_url = "http://0.0.0.0:5000"


@app.route("/get_ip")
def get_up():
    ip_address = sys_handler.get_ip()
    return jsonBuilder.ip_to_json(ip_address)


@app.route("/login", methods=['POST'])
def login():
    if request.form['password'] == "kocka":
        session['logged_in'] = True
        return redirect("/")
    return redirect("/login_page")


@app.route("/login_page")
def login_page():
    list_of_messages = ['LEPJ BE HA TUDSZ',
                        "TUDOD A JELSZÓT?",
                        "TALÁN HA SZÉPEN KÉRED",
                        "KÉNE A JELSZÓ MI",
                        "YOU SHALL NOT PASS",
                        "EZEK ITT TITKOS FÁLJOK",
                        ]
    return render_template("login.html", message=list_of_messages[random.randrange(len(list_of_messages) - 1)])


@app.route("/")
def index():
    if "logged_in" not in session:
        return redirect("login_page")
    return render_template("index2.html")


@app.route("/get_folders", methods=['POST'])
def get_folders():
    location = request.form['currentLocation']
    list_of_folders = sys_handler.get_folder_dict(location)['folders']
    list_of_folders.sort()
    return jsonBuilder.folders_to_json(list_of_folders)


@app.route("/get_files_with_size", methods=['POST'])
def get_files_with_size():
    location = request.form['currentLocation']
    list_of_file_dicts = sys_handler.get_files_with_stat(location)
    return jsonify(list_of_file_dicts)


@app.route("/get_files", methods=['POST'])
def get_files():
    location = request.form['currentLocation']
    list_of_files = sys_handler.get_folder_dict(location)['files']
    list_of_files.sort()
    return jsonBuilder.files_to_json(list_of_files)


@app.route("/get_location")
def get_location():
    path = sys_handler.get_current_path()
    return jsonBuilder.location_to_json(path)


@app.route("/download_file/<path>")
def download_file(path):
    folder_name = None
    file_name = None
    real_path = path.replace("!", "/")
    for x in range(len(real_path) - 1, -1, -1):
        if real_path[x] == "/":
            folder_name = real_path[0:x + 1]
            file_name = real_path[x + 1:]
            break
    if folder_name is None or file_name is None:
        print("folder name or file name is not correct")
    try:
        return send_from_directory(folder_name, file_name, as_attachment=True)
    except Exception as e:
        print(e)


@app.route("/compress_folder/<path>")
def compress_folder(path):
    path = path.replace("!", "/")
    char_index = None
    for i in range(len(path) - 1, 0, -1):
        if path[i] == "/":
            char_index = i
            break
    if char_index is None:
        print("Invalid path")
    return send_file(shutil.make_archive(path[char_index + 1:], "zip", path), as_attachment=True)


if __name__ == "__main__":
    app.secret_key = "app_magic"
    app.run(
        host='0.0.0.0',
        debug=True,
        threaded=True,
        port=5000
    )
