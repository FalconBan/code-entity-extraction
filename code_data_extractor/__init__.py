from . import read_and_extract_data
from . import class_data_holder
import argparse

parser = argparse.ArgumentParser(description='Read the file name')
parser.add_argument('file_name', metavar='file_name', type=str, nargs='+',
                    help='File for which the tokens should be extracted')
parser.add_argument('--file', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()