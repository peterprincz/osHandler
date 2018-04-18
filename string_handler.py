def convert_parampath_to_realpath(parampath):
    return parampath.replace("!", "/")


def get_folder_name(path):
    for i in range(len(path) - 1, 0, -1):
        if path[i] == "/":
            char_index = i
            return path[char_index + 1:]


def get_folder_and_file(path):
    result = {}
    for x in range(len(path) - 1, -1, -1):
        if path[x] == "/":
            result["folder_name"] = path[0:x + 1]
            result["file_name"] = path[x + 1:]
            return result