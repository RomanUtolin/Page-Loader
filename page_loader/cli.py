import argparse
import os


def get_parser():
    parser = argparse.ArgumentParser(description='Loader Url Pages')
    parser.add_argument('url')
    parser.add_argument('-o',
                        '--output',
                        dest='output',
                        default=os.getcwd(),
                        help='set output directory'
                        )
    parser.add_argument('-l',
                        '--log-level',
                        dest='level',
                        default='info',
                        help='set logging level',
                        )
    return parser
