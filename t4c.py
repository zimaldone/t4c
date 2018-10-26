#!/usr/bin/env python
"""
Script to convert CSV input data in JSON
"""
from __future__ import print_function, division
import csv
import sys
import logging
import operator
from t4c.validate import fields_validation
from t4c.validate import file_check
from t4c.util import args_parser
from t4c.util import json_util


# setup logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
                    , level=logging.INFO)
LOGGER = logging.getLogger(__name__)


def reader(source_file):
    """
    Reads source `filename` and returns a DictReader object
    it raises IOError exception `filename` cannot be read
    """
    try:
        with open(source_file, mode='r') as hotels_file:
            return csv.DictReader(hotels_file, delimiter=',')
    except IOError as e:
        print ("I cannot read {} or it does not exists".format(source_file))
        # raise HotelException(msg)


def data_parser(data_read):
    """
    takes `reader` and returns a list of valid item
    """
    data = []
    for row in data_read:
        # if valid(row):
        data.append(row)

        # for testing...
        if len(data) > 10:
            break
    return data


def write_data(data_parsed, destination_json, sort_by_field, fields_name):
    data_parsed.sort(key=operator.itemgetter(
                    fields_validation.field_exists_in_csv_fields(sort_by_field, fields_name)))

    if file_check.write_existing_file(destination_json):
        json_util.write_json_to_file(data_parsed, destination_json)


def main():
    args = args_parser.parse_cli()

    # TODO make sure it runs everywhere
    # TODO unit test (pytest)
    # TODO support yaml pyYaml

    destination_json = args.destination_file
    source_file = args.source_file
    sort_by_field = args.sort_by_field

    file_check.delete_file(destination_json)

    data_read = reader(source_file)
    fields_name = data_read.fieldnames
    data_parsed = data_parser(data_read)
    write_data(data_parsed, destination_json, sort_by_field, fields_name)

    print('\n\n#############################################')
    print("I saved and validated for you {} hotels!!".format(len(data_parsed)))


if __name__ == '__main__':
    try:
        main()
    except GeneratorExit:
        sys.exit(1)
