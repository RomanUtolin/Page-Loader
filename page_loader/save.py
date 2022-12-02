import logging


def save_html(html, path):
    with open(path, 'w') as file:
        file.write(html)
        logging.info(f'Saved html to {path}')
    return path


def save_file(file, path):
    with open(path, 'wb') as f:
        f.write(file)
        logging.info(f'Saved file to {path}')
    print(path)
