#!/usr/bin/env python
"""
Script to convert CSV input data in JSON
"""
from __future__ import print_function, division
import sys
import operator
import csv
import t4c.validate as validate
import t4c.util as util

# TODO h name may only contain UTF-8 characters.
# ---
# TODO make sure it runs everywhere
# TODO unit test (pytest)
# TODO support yaml pyYaml


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
                    print(str(len(data)) + ' - ' + row['name'] + ' - ' + row['uri'])
                    data.append(validate_data(row, complex_url_validation))

                    # for test
                    if len(data) >= 20:
                        break

                except (StopIteration, BaseException) as ex:
                    not_valid.append(row)

            return reader.fieldnames, data, not_valid

    except IOError as ioe:
        raise GeneratorExit("!!! - ooops  I cannot read {} or it does not exists".format(ioe.filename))


def validate_data(current_row, complex_url_validation):
    """ this function is currently quite 'dumb'
        using hard-coded values and triggering the right validation """

    try:
        current_row['name'] = current_row['name']
        current_row['address'] = current_row['address']
        current_row['stars'] = validate.rating_validation(current_row['stars'])
        current_row['contact'] = current_row['contact']
        current_row['phone'] = current_row['phone']
        current_row['uri'] = validate.url_validation(current_row['uri'], complex_url_validation)
        return current_row
    except (validate.StarsValidationError, validate.UriValidationError) as si:
        print(si.message)
        raise StopIteration


def write_data(data_parsed, destination_json, sort_by_field, fields_name):
    if sort_by_field != 'None':
        data_parsed.sort(key=operator.itemgetter(validate.field_exists_in_csv_fields(sort_by_field, fields_name)))
    util.write_json_to_file(data_parsed, destination_json)


def main():
    args = util.args_parser.parse_cli()
    destination_json = args.destination_file
    failed_validation_file = util.file_check.get_invalid_hotels_file()
    source_file = args.source_file
    sort_by_field = str(args.sort_by_field)
    complex_url_validation = args.complex_url_validation

    # For test
    util.delete_file(destination_json)

    # let's crack this down :)
    data_read_and_parsed = read_and_parse(source_file, complex_url_validation)

    fields_name = data_read_and_parsed[0]
    data_processed = data_read_and_parsed[1]
    data_failed_validation = data_read_and_parsed[2]

    # Finally Write data
    write_data(data_processed, destination_json, sort_by_field, fields_name)
    write_data(data_failed_validation,failed_validation_file, sort_by_field, fields_name)

    print('\n\n#############################################')
    print("I saved and validated for you {} hotels!!".format(len(data_read_and_parsed[1])))
    print("Unfortunately {} hotels did not pass the validation".format(len(data_failed_validation)))


if __name__ == '__main__':
    try:
        main()
    except GeneratorExit as gex:
        print(gex.message)
        sys.exit(1)
