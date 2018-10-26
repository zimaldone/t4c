#!/usr/bin/env python
"""
Script to convert CSV input data in JSON
"""
from __future__ import print_function, division
import csv
import sys
import logging
import operator
from validation import fields_validation
# from encoding import encoder_decoder
from util import json_util, args_parser
from validation import file_check


# setup logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
                    , level=logging.INFO)
LOGGER = logging.getLogger(__name__)


def main():
    args = args_parser.parse_cli()
    try:
        # TODO make sure it runs everywhere
        # TODO unit test (pytest)
        # TODO support yaml pyYaml

        destination_json = args.destination_file
        source_file = args.source_file
        sort_field = args.sort_by_field

        file_check.delete_file(destination_json)
        i = 0
        if file_check.read_existing_file(source_file):
            my_hotels = []
            with open(source_file, mode='r') as hotels_file:
                reader = csv.DictReader(hotels_file, delimiter=',')
                # print(reader.fieldnames)
                for row in reader:
                    my_hotels.append(row)
                    i += 1
                    if i == 10:
                        break
                    my_hotels.sort(key=operator.itemgetter(
                        fields_validation.field_exists_in_csv_fields(sort_field, reader.fieldnames)))

            if file_check.is_current_dir_writeable():
                if file_check.write_existing_file(destination_json):
                    json_util.write_json_to_file(my_hotels, destination_json)

        print('\n\n#############################################')
        print("I saved and validated for you {} hotels!!".format(i))
    except IOError as error:
        print('error!!! -> {}'.format(error))
        sys.exit(1)


if __name__ == '__main__':
    main()
