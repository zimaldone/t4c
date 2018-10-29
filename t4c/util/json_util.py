import json


def write_json_to_file(data, destination_file):
    try:
        with open(destination_file, 'w') as file_dest:
            json.dump(data, file_dest, indent=4, encoding='utf-8', ensure_ascii=False)

    except IOError as err:
        raise IOError("Ooops - There has been an error writing {}".format(err.filename))
