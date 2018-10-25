import json
import logging


LOGGER = logging.getLogger(__name__)


def read_json_from_file(file, default=None):
    LOGGER.info('Reading file {}'.format(file))
    try:
        with open(file) as f:
            return json.load(f)
    except IOError:
        LOGGER.warning('Could not open {}, returning default value!'.format(file))
        return default


def write_json_to_file(data, file,sort_keys):
    with open(file, 'w') as f:
        json.dump(data, f, sort_keys=sort_keys, indent=4)