import jsonBuilder
import sys_handler
from flask import Flask, render_template, redirect, request, session, jsonify, send_file, send_from_directory
import os

app = Flask(__name__)
current_url = "http://127.0.0.1:5000"

@app.route("/api_index")
def api_index():
    result = {"location" : current_url + "/get_location",
              "get_files": current_url + "/get_files",
              "get_folders": current_url + "/get_folders",
              "move back" : current_url + "/move_back"}
    return jsonify(result)


@app.route("/")
def index():
    return render_template("index2.html")


@app.route("/ajaxtest")
def test():
    print(request.form['value'])
    return jsonify({"value": "key"})


@app.route("/get_folders", methods=['POST'])
def get_folders():
    location = request.form['currentLocation']
    list_of_folders = sys_handler.get_folder_dict(location)['folders']
    print(list_of_folders)
    return jsonBuilder.get_folders(list_of_folders)


@app.route("/get_files", methods=['POST'])
def get_files():
    location = request.form['currentLocation']
    list_of_files = sys_handler.get_folder_dict(location)['files']
    return jsonBuilder.get_files(list_of_files)


#---------------------------------------------------------------------------------------------------------
@app.route("/move_to/<foldername>")
def move_into_folder(foldername):
    sys_handler.move_into_folder(foldername)
    return jsonBuilder.get_location()


@app.route("/get_location")
def get_location():
    return jsonBuilder.get_location()


@app.route("/download_file/<path>")
def DownloadLogFile (path):
    realpath = path.replace("!", "/")
    try:
        return send_from_directory(os.getcwd(), realpath, as_attachment=True)
    except Exception as e:
        print(e)


@app.route("/move_back")
def move_back():
    sys_handler.move_back()
    return jsonBuilder.get_location()


@app.route("/compress_folder/<foldername>")
def compress_folder(foldername):
    sys_handler.compress_folder(foldername)
    print(os.getcwd())
    print(foldername)
    return send_from_directory(os.getcwd(), foldername +".zip", as_attachment=True)


if __name__ == "__main__":
    app.secret_key = "app_magic"  # Change the content of this string
    app.run(
        host = '0.0.0.0',
        debug=True,
        port=5000
    )
