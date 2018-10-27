import os


def write_existing_file(file_path):

    # TODO REFACTORING HERE TO RAISE RIGHT EXCEPTIONS

    if os.path.isfile(file_path) and os.path.exists(file_path) and os.access(file_path, os.W_OK):
        choice = raw_input('\n\nDo you want to overwrite the file? [ Y | N ]').lower()
        if choice == "y" or choice == "yes":
            return True
    else:
        if is_current_dir_writeable():
            print("File {} is currently not existing."
                  " I'm going to create it for you".format(file_path))
            return True
        else:
            print("Ooops ... I cannot write {} in this folder!!".format(file_path))

    print("File {} won't be overwritten".format(file_path))
    return False


def is_current_dir_writeable():
    if not os.access(os.pardir, os.W_OK):
        print("ehy man... I cannot write in this Directory")
        return False
    else:
        return True


def delete_file(file_to_delete):
    try:
        os.remove(file_to_delete)
    except (IOError, WindowsError) as ioe:
        print ("Ooops - There has been an error deleting {}".format(ioe.filename))
        pass
