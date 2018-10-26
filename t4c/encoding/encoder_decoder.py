

def make_unicode(input_to_encode):
    if type(input_to_encode) is not unicode:
        input_to_encode = unicode(input_to_encode,'utf-8')
        return input_to_encode
    else:
        return input_to_encode
