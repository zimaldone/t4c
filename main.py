#!/usr/bin/env python
"""
q....
"""
from __future__ import print_function, division
import csv, sys, logging
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
        # TODO sort List
        # TODO unit test pytest)
        # TODO support yaml pyYaml

        destination_json = args.destination_file
        source_file = args.source_file
        if file_check.file_validation_read(source_file):
            my_hotels = []
            with open(source_file, mode='r') as hotels_file:
                reader = csv.DictReader(hotels_file, delimiter=',')
                # print(reader.fieldnames)
                for row in reader:
                    # print(row['name'], row['address'])
                    # print(row)
                    # print(dir(row))
                    print (row)
                    my_hotels.append(row)
                    break
            if file_check.is_current_dir_writeable():
                if file_check.file_validation_read(destination_json):
                    choice = raw_input('Do you want to overwrite the file? [Y|N]').lower()
                    if choice == "n" or choice != "y":
                        sys.exit()
                    else:
                        json_util.write_json_to_file(my_hotels, destination_json, "True")
                else:
                    print("Input File {} not found!!".format(source_file))
            else:
                print("ehy man... I cannot write in this Directory")
    except IOError as error:
        print('error!!! -> {}'.format(error))
        sys.exit(1)


if __name__ == '__main__':
    main()
