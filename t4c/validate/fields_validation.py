import socket
import time
import logging
import timeit
import validators
import tldextract
import t4c.t4c_exceptions as t4c_ex


LOGGER = logging.getLogger(__name__)


def field_exists_in_csv_fields(single_field, list_fields):
    if single_field in list_fields:
        return single_field
    return "name"


def rating_validation(hotel_stars):
    """check if stars are in valid range"""
    hotel_stars = int(hotel_stars)
    if validators.between(hotel_stars, 0, 5):
        return hotel_stars
    else:
        raise t4c_ex.StarsValidationError("Stars {} is not valid".format(hotel_stars))


def url_validation(hotel_uri, complex_validation):
    """ check if syntactically the URL is valid.
        if the "complex validation" is enabled it checks
        if the Top Level Domain (TLD) is resolvable """
    t1 = timeit.default_timer()
    try:
        if validators.url(hotel_uri):
            if complex_validation:
                url_complex_validation(hotel_uri)
        else:
            raise t4c_ex.UriValidationError("The URL {} is not a valid one".format(hotel_uri))
    except (t4c_ex.UriValidationError, socket.gaierror) as ex:
        if type(ex).__name__ == 'gaierror':
            ex.message = "The address for {} cannot be resolved - Time spent {}"\
                .format(hotel_uri, timeit.default_timer() - t1)
        raise t4c_ex.UriValidationError(ex.message)

    LOGGER.debug("url_validation performance {}".format(timeit.default_timer() - t1))
    return hotel_uri


def url_complex_validation(hotel_uri):
    domain = tldextract.extract(hotel_uri).registered_domain
    socket.setdefaulttimeout(3)
    ip_resolved = socket.gethostbyname(domain)
    time.sleep(0.05)   # to avoid the hammering of DNS service
    if validators.ip_address.ipv4(ip_resolved) or validators.ip_address.ipv6(ip_resolved):
        return


def cast_str_2_boolean_argument(arg):
    if not isinstance(arg, bool):
        if arg.lower() == 'false' or arg.lower() == 'f':
            return False
        elif arg.lower() == 'true' or arg.lower() == 't':
            return True
        else:
            raise RuntimeError("Invalid argument")
    else:
        return arg
