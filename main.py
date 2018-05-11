from werkzeug.utils import secure_filename


import sys_handler
import service

from flask import Flask, request, send_file, send_from_directory

app = Flask(__name__)


@app.route("/get_ip")
def get_ip():
    return service.get_ip()


@app.route("/get_butterfly_address")
def get_butterfly_address():
    return service.get_butterfly_address()


@app.route("/start_butterfly")
def butterfly():
    sys_handler.launch_butterfly()
    return service.get_butterfly_address()


@app.route("/")
def index():
    return app.send_static_file('templates/index2.html')


@app.route("/get_folders", methods=['POST'])
def get_folders():
    return service.get_folders(request)


@app.route("/get_files_with_size", methods=['POST'])
def get_files_with_size():
    return service.get_files_with_size(request)


@app.route("/get_files", methods=['POST'])
def get_files():
    return service.get_files(request)


@app.route("/get_root_path")
def get_location():
    return service.get_location()


@app.route("/download_file/<path>")
def download_file(path):
    file_infos = service.get_file_for_download(path)
    folder_name = file_infos["folder_name"]
    file_name = file_infos["file_name"]
    if folder_name is None or file_name is None:
        return "File not found", 404
    try:
        return send_from_directory(folder_name, file_name, as_attachment=True)
    except Exception as e:
        app.logger.critical(e)
        return "Internal server error", 500


@app.route("/compress_folder/<path>")
def compress_folder(path):
    return send_file(service.make_rar_for_download(path), as_attachment=True)


@app.route('/upload_file/<path>', methods=['GET', 'POST'])
def upload_file(path):
    if request.method != 'POST':
        return 'Bad request', 300
    file = request.files['file']
    if file is None:
        return 'Error while accesing file', 500
    service.save_file(file, path)
    return 'OK', 200


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


