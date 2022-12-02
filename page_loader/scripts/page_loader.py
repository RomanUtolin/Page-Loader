import sys
import logging
from page_loader import cli, loading

LEVELS = {
    'info': 'INFO',
    'debug': 'DEBUG',
    'warning': 'WARNING',
    'error': 'ERROR'
}


def setup(log_level):
    logging.basicConfig(
        level=logging.getLevelName(LEVELS[log_level]),
    )


def main():
    parser = cli.get_parser()
    args = parser.parse_args()
    setup(args.level)
    try:
        print(loading.download(args.url, args.output))
    except Exception as error:
        logging.error(f"Failed: {error}")
        sys.exit(1)


if __name__ == "__main__":
    main()
