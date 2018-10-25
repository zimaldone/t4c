import os


def file_validation_read(file_path):
        return os.path.isfile(file_path) and os.path.exists(file_path) and os.access(file_path, os.R_OK)


def is_current_dir_writeable ():
    return os.access(os.pardir,os.W_OK)