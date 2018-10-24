import json

def write_json_to_file(data, file):
    # logger.info('Writing {}'.format(file))
    with open(file, 'w') as f:
        json.dump(data, f, sort_keys=True, indent=4)