import json


def read_json_from_file(input_file, default=None):
    try:
        with open(input_file) as f:
            return json.load(f)
    except IOError:
        return default


def write_json_to_file(data, destination_file):
    try:
        with open(destination_file, 'w') as f:
            json.dump(data, f, indent=4, encoding='utf-8')
    except IOError as e:
        raise GeneratorExit("Ooops - There has been an error writing {}".format(e.filename))
