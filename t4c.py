#!/usr/bin/env python
"""
Script to convert CSV input data in JSON
"""
from __future__ import print_function, division
import sys
import operator
from csv import DictReader
import t4c.encoding
from t4c.validate import fields_validation
from t4c.validate import file_check
from t4c.util import args_parser
from t4c.util import json_util

# TODO UNICODE / UTF-8 issue
# TODO validate url
# TODO make sure it runs everywhere
# TODO unit test (pytest)
# TODO support yaml pyYaml


def utf_8_encoder(unicode_csv_data):
    for line in unicode_csv_data:
        yield line.encode('utf-8')


def read_and_parse(source_file):
    """
    Reads source `filename` and returns a tuple with 2 elements
    0 - list with CSV Fields names
    1 - List of Dicts with all the row-elements

    It raises IOError exception `filename` cannot be read
    """
    try:
        with open(source_file, mode='r') as hotels_file:
            reader = DictReader(utf_8_encoder(hotels_file), delimiter=',')
            return reader.fieldnames, data_parser(reader)

    except IOError as ioe:
        raise GeneratorExit("!!! - ooops  I cannot read {} or it does not exists".format(ioe.filename))


def data_parser(data_read):
    """
    takes `reader` and returns a list of valid item
    """
    data = []
    for row in data_read:
        # if valid(row):
        data.append(row)

        # for testing...
        if len(data) >= 10:
            break
    return data


def write_data(data_parsed, destination_json, sort_by_field, fields_name):
    # type: (list, str, str, list) -> None

    data_parsed.sort(key=operator.itemgetter(
                    fields_validation.field_exists_in_csv_fields(sort_by_field, fields_name)))
    json_util.write_json_to_file(data_parsed, destination_json)


def main():
    args = args_parser.parse_cli()

    destination_json = args.destination_file
    source_file = args.source_file
    sort_by_field = args.sort_by_field

    file_check.delete_file(destination_json)

    data_read_and_parsed = read_and_parse(source_file)
    write_data(data_read_and_parsed[1], destination_json, sort_by_field, data_read_and_parsed[0])

    print('\n\n#############################################')
    print("I saved and validated for you {} hotels!!".format(len(data_read_and_parsed[1])))


if __name__ == '__main__':
    try:
        main()
    except GeneratorExit as gex:
        print(gex.message)
        sys.exit(1)
