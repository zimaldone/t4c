import t4c.t4c_exceptions as tc4_ex


def is_a_utf8_string(input_str):
    try:
        input_str.decode('UTF-8', errors="replace")  # enforcing UTF-8
        return input_str
    except UnicodeDecodeError:
        raise tc4_ex.NotUTF8Error("UTF-8 string {} and len is {}".format(input_str, len(input_str)))