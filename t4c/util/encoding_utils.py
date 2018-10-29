import t4c.t4c_exceptions as tc4_ex


def is_a_utf8_string(input_str):
    try:
        input_str.decode('utf-8')
        print("Unicode {} and UTF-8 string len is {}".format(unicode(input_str), len(input_str)))
        return input_str
    except UnicodeDecodeError:
        raise tc4_ex.NotUTF8Error("Unicode {} and UTF-8 string len is {}".format(unicode(input_str), len(input_str)))
