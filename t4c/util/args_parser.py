import argparse
import os
from file_check import DATA_DIR
"""Parse command line options"""


def parse_cli():
    """Parse command line options"""

    parser = argparse.ArgumentParser(description="Hotel Data Conversion: It converts and"
                                                 " validate data from CSV file to JSON"
                                                 "\n\n-> Default Input file: hotels.csv"
                                                 "\n-> Default Output Json: hotels.json",
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-s", "--source-file", required=False,
                        default=os.path.join(os.getcwd(), DATA_DIR, "hotels.csv"))

    parser.add_argument("-d", "--destination-file", required=False,
                        default=os.path.join(os.getcwd(), DATA_DIR, 'hotels.json'))

    parser.add_argument("--sort-by-field", required=False, default='None',
                        help='The field in INPUT file that you want to use to sort the OUTPUT file')

    parser.add_argument("--complex-url-validation", required=False, default=False,
                        help='It uses additional logic to asses and URI passed, '
                             'like testing the availability of the TLD')

    return parser.parse_args()
