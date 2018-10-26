import os


def read_existing_file(file_path):
        if os.path.isfile(file_path) and os.path.exists(file_path) and os.access(file_path, os.R_OK):
            return True
        else:
            print("I cannot read {} or it does not exists".format(file_path))
            return False


def write_existing_file(file_path):
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
    if read_existing_file(file_to_delete):
        os.remove(file_to_delete)