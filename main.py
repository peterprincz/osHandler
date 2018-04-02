import jsonBuilder
import sys_handler
from flask import Flask, render_template, redirect, request, session, jsonify, send_file, send_from_directory
import os
import shutil

app = Flask(__name__)
current_url = "http://0.0.0.0:5000"

@app.route("/")
def index():
    return render_template("index2.html")


@app.route("/get_folders", methods=['POST'])
def get_folders():
    location = request.form['currentLocation']
    list_of_folders = sys_handler.get_folder_dict(location)['folders']
    return jsonBuilder.get_folders(list_of_folders)


@app.route("/get_files", methods=['POST'])
def get_files():
    location = request.form['currentLocation']
    list_of_files = sys_handler.get_folder_dict(location)['files']
    return jsonBuilder.get_files(list_of_files)


@app.route("/get_location")
def get_location():
    return jsonBuilder.get_location()


@app.route("/download_file/<path>")
def DownloadLogFile (path):
    foldername = ""
    filename = ""
    realpath = path.replace("!", "/")
    for x in range(len(realpath) - 1, -1, -1):
        if realpath[x] == "/":
            foldername = realpath[0:x + 1]
            filename = realpath[x + 1:]
            break
    if foldername == "" or filename == "":
        print("foldername or filename is not found")
    try:
        return send_from_directory(foldername, filename, as_attachment=True)
    except Exception as e:
        print(e)


@app.route("/compress_folder/<path>")
def compress_folder(path):
    path = path.replace("!", "/")
    char_index = None
    for i in range(len(path) - 1, 0, -1):
        if (path[i] == "/"):
            char_index = i
            break
    return send_file(shutil.make_archive(path[char_index + 1:], "zip", path), as_attachment=True)


@app.route("/api_index")
def api_index():
    result = {"location" : current_url + "/get_location",
              "get_files": current_url + "/get_files",
              "get_folders": current_url + "/get_folders",
              "move back" : current_url + "/move_back"}
    return jsonify(result)


if __name__ == "__main__":
    app.secret_key = "app_magic"  # Change the content of this string
    app.run(
        host = '0.0.0.0',
        debug=True,
        port=5000
    )
