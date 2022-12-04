import logging


def save(content, path):
    if isinstance(content, bytes):
        mode = 'wb'
    else:
        mode = 'w'
        print(path)
    with open(path, mode) as file:
        file.write(content)
        logging.info(f'Saved to {path}')
    return path
