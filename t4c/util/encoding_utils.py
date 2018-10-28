

def is_a_utf8_string(input_str):
    valid_utf8 = ''
    try:
        input_str.decode('utf-8')
        print("Unicode {} and UTF-8 string len is {}".format(unicode(input_str), len(input_str)))
        valid_utf8 = True
    except UnicodeDecodeError:
        print("Unicode {} and UTF-8 string len is {}".format(unicode(input_str), len(input_str)))
        valid_utf8 = False
    finally:
        return valid_utf8
