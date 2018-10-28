import validators
import socket
import tldextract
import time


class StarsValidationError(StopIteration):
    pass


class UriValidationError(StopIteration):
    pass


def field_exists_in_csv_fields(single_field, list_fields):
    if single_field in list_fields:
        return single_field
    return "name"


def stars_validation(hotel_stars):
    """check if stars are in valid range"""

    hotel_stars = int(hotel_stars)
    if validators.between(hotel_stars, 0, 5):
        return hotel_stars
    else:
        raise StarsValidationError("Stars {} is not valid".format(hotel_stars))


def url_validation(hotel_uri, complex_validation):
    """ check if syntactically the URL is valid.
        if the "complex validation" is enabled it checks
        if the Top Level Domain (TLD) is resolvable """
    try:
        if validators.url(hotel_uri):
            if complex_validation:
                return url_complex_validation(hotel_uri)
        else:
            raise UriValidationError("The URL {} is not a valid one".format(hotel_uri))

    except (UriValidationError, socket.gaierror) as ex:
        # print("An exception of type {0} occurred. Arguments:\n{1!r}".format(type(ex).__name__, ex.args))
        raise UriValidationError(ex.message)


def url_complex_validation(hotel_uri):
    domain = tldextract.extract(hotel_uri).registered_domain
    ip_resolved = socket.gethostbyname(domain)
    # time.sleep(0.1)
    if validators.ip_address.ipv4(ip_resolved) or validators.ip_address.ipv6(ip_resolved):
        return hotel_uri


# if not util.is_a_utf8_string(row['name']):
#     print('NO UTF8 STRING!!! {}'.format(row['name']))
