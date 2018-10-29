import os
import logging

DATA_DIR = 'data'

logger = logging.getLogger(__name__)


class NoOverwriteError(GeneratorExit):
    pass


def write_existing_file(overwrite_destination, filename):

    if os.path.isfile(filename) and os.path.exists(filename):
        if overwrite_destination:
            return
        else:
            raise NoOverwriteError("File {} won't be overwritten".format(filename))


def is_current_dir_writeable():
    if not os.access(os.pardir, os.W_OK):
        print("ehy man... I cannot write in this Directory")
        return False
    else:
        return True


def get_invalid_hotels_file():
    data_dir = os.path.join(os.getcwd(), DATA_DIR)
    if os.access(data_dir, os.W_OK):
        return os.path.join(data_dir, "invalid_hotels.json")


def get_data_folder():
    return os.path.join(os.getcwd(), DATA_DIR)


def delete_file(file_to_delete):
    try:
        os.remove(file_to_delete)
    except (IOError, WindowsError) as ioe:
        print ("Ooops - There has been an error deleting {}".format(ioe.filename))
        pass
