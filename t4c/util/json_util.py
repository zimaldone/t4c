import json


def write_json_to_file(data, destination_file):
    try:
        with open(destination_file, 'w') as f:
            json.dump(data, f, indent=4, encoding='utf-8', ensure_ascii=False)

    except IOError as e:
        raise IOError("Ooops - There has been an error writing {}".format(e.filename))
