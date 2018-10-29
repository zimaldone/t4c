import argparse
import os
from t4c.util.file_checks import DATA_DIR
"""Parse command line options"""


def parse_cli():
    """Parse command line options"""

    parser = argparse.ArgumentParser(description="Hotel Data Conversion: It converts and"
                                                 " validate data from CSV file to JSON"
                                                 "\n\n-> Default Input file: .data/hotels.csv"
                                                 "\n-> Default Output Json: .data/hotels.json",
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-s", "--source-file", required=False,
                        default=os.path.join(os.getcwd(), DATA_DIR, "hotels.csv"))

    parser.add_argument("-d", "--destination-file", required=False,
                        default=os.path.join(os.getcwd(), DATA_DIR, 'hotels.json'))

    parser.add_argument("--overwrite-destination-file", required=False,
                        default=True, choices=['True', 'False'])

    parser.add_argument("--sort-by-field", required=False, default='None',
                        help='The field in INPUT file that '
                             'you want to use to sort the OUTPUT file')

    parser.add_argument("--complex-url-validation", required=False,
                        default=False, choices=['True', 'False'],
                        help='Default = False - '
                             'It uses additional logic to evaluate the URL passed\n'
                             'WARNING - It slows down drastically script performance')

    return parser.parse_args()
