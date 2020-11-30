import pathlib
import json


def save_dictionary(dict, file_path):
    with open(file_path, "w") as file:
        file.write(json.dumps(dict))


def read_dictionary(file_name):
    with open(file_name, "r") as file:
        dict_file = json.loads(file.read())
        return sorted(dict_file)


if __name__ == '__main__':
    dict = {2: "2", 1: "1"}
    path = pathlib.Path().absolute()
    filePath = str(path) + "/" + "save_dict.txt"

    save_dictionary(dict, str(filePath))
    print(read_dictionary(filePath))
