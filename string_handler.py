import datetime


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


def humanTime(time):
    return datetime.datetime.fromtimestamp(int(time)).strftime("%Y-%m-%d %H:%M:%S")
