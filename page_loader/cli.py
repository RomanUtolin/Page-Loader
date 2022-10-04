import argparse
import os
from page_loader.loader import download


def get_parser():
    parser = argparse.ArgumentParser(description='Loader url pages')
    parser.add_argument('url')
    parser.add_argument('-o', '--output',
                        dest='output',
                        default=os.getcwd()
                        )
    arg = parser.parse_args()
    print(download(arg.url, arg.output))
