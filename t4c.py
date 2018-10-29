#!/usr/bin/env python
"""
Script to convert CSV input data in JSON
"""
from __future__ import print_function, division
import sys
import operator
import csv
import logging
import timeit
import t4c.t4c_exceptions as t4c_ex
import t4c.validate as validate
import t4c.util as util

# TODO h name may only contain UTF-8 characters.
# ---
# TODO make sure it runs everywhere
# TODO unit test (pytest)
# TODO support yaml pyYaml

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)


def utf_8_encoder(unicode_csv_data):
    for line in unicode_csv_data:
        yield line.encode('utf-8')


def read_and_parse(source_file, complex_url_validation):
    """
    Reads source `filename` and returns a tuple with 2 elements
    0 - list with CSV Fields names
    1 - List of Dicts with all the row-elements
    It raises IOError exception `filename` cannot be read
    """
    try:
        with open(source_file, mode='r') as hotels_file:
            reader = csv.DictReader(hotels_file, delimiter=',')
            data = []
            not_valid = []
            for row in reader:
                try:
                    logger.debug(str(len(data)) + ' - ' + row['name'] + ' - ' + row['uri'])
                    data.append(validate_data(row, complex_url_validation))
                    # for test
                    # if len(data) >= 100:
                    #   break

                except t4c_ex.GenericT4cError as ex:
                    not_valid.append(row)
            return reader.fieldnames, data, not_valid
    except IOError as ioe:
        raise IOError("!!! - ooops  I cannot read {} or it does not exists".format(ioe.filename))


def validate_data(current_row, complex_url_validation):
    """ this function is currently quite 'dumb'
        using hard-coded values and triggering the right validation """
    try:
        current_row['name'] = util.is_a_utf8_string(current_row['name'])
        current_row['address'] = current_row['address']
        current_row['stars'] = validate.rating_validation(current_row['stars'])
        current_row['contact'] = current_row['contact']
        current_row['phone'] = current_row['phone']
        current_row['uri'] = validate.url_validation(current_row['uri'], complex_url_validation)
        return current_row
    except (t4c_ex.StarsValidationError, t4c_ex.UriValidationError, t4c_ex.NotUTF8Error) as si:
        logger.error(si.message)
        raise t4c_ex.GenericT4cError


def write_data(data_parsed, destination_json, sort_by_field, fields_name):
    if sort_by_field != 'None':
        data_parsed.sort(key=operator.itemgetter(validate.field_exists_in_csv_fields(sort_by_field, fields_name)))
    util.write_json_to_file(data_parsed, destination_json)


def main():
    args = util.args_parser.parse_cli()
    destination_json = args.destination_file
    failed_validation_file = util.file_checks.get_invalid_hotels_file()
    source_file = args.source_file
    sort_by_field = str(args.sort_by_field)
    overwrite_destination = validate.cast_str_2_boolean_argument(args.overwrite_destination_file)
    complex_url_validation = validate.cast_str_2_boolean_argument(args.complex_url_validation)

    if logger.level == logging.DEBUG:
        for arg in vars(args):
            logger.info("Starting with parameters: {} - {}".format(arg, getattr(args, arg)))
            logger.info("\n################################\n")

    util.write_existing_file(overwrite_destination, destination_json)

    st1 = timeit.default_timer()
    # let's crack this down :)
    data_read_and_parsed = read_and_parse(source_file, complex_url_validation)
    fields_name = data_read_and_parsed[0]
    data_processed = data_read_and_parsed[1]
    data_failed_validation = data_read_and_parsed[2]

    # Finally Write data
    write_data(data_processed, destination_json, sort_by_field, fields_name)
    # for the time being to make it simple, Always overwrite invalid hotels' file
    write_data(data_failed_validation,failed_validation_file, sort_by_field, fields_name)

    st2 = timeit.default_timer()

    logger.info('\n\n#############################################')
    logger.info("I saved and validated {} hotels in {} seconds".format(len(data_read_and_parsed[1]), st2-st1))
    logger.info("Unfortunately {} hotels did not pass the validation".format(len(data_failed_validation)))
    logger.info("You can find all the generated data inside {}".format(util.get_data_folder()))


if __name__ == '__main__':
    try:
        t1 = timeit.default_timer()
        main()
        t2 = timeit.default_timer()
        logger.info("Overall script took: {} seconds".format(t2-t1))
    except (GeneratorExit, IOError, RuntimeError) as error:
        print(error)
        sys.exit(1)
