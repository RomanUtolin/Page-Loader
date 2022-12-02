import logging


def save(content, path):
    write_mode = 'wb' if isinstance(content, bytes) else 'w'
    with open(path, write_mode) as file:
        file.write(content)
        logging.info(f'Saved to {path}')
    return path
