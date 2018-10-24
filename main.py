#!/usr/bin/env python
"""
q....
"""
from __future__ import print_function, division

import csv, sys, json
from encoding import encoder_decoder
from util.json_util import write_json_to_file
import argparse

def parse_cli():
        """parse command line options"""
        parser = argparse.ArgumentParser(description="best hotel: helps you to find tgheahsdghsjg")
        parser.add_argument("-s", "--source-file", required=True, default='hotels.csv')
        return parser.parse_args()

def main():
   args = parse_cli()
   try:
        ## TODO Check if file exists
        ## TODO sort List
        ## TODO unit test pytest)
        ## TODO make sure it runs everywhere
        ## TODO support yaml pyYaml

        destination_json = 'hotel.json'
        source_file = args.source_file
        my_hotels = []
        with open(source_file, mode='r') as hotels_file:
                reader = csv.DictReader(hotels_file, delimiter=',')
                print(reader.fieldnames)
                for row in reader:
                        #print(row['name'], row['address'])
                        #print(row)
                        #print(dir(row))
                        my_hotels.append(row)
                        break
        write_json_to_file(my_hotels,destination_json)
        # https://docs.python.org/2/library/urlparse.html
   except IOError as error:
        print('error!!! -> {}'.format(error))
        sys.exit(1)

if __name__ == '__main__':
    main()