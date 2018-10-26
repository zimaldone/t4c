import argparse
import os

DATA_DIR = 'data'


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
    parser.add_argument("--sort-by-field", required=False, default='name')
    return parser.parse_args()