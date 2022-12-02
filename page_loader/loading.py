import re
import os
import requests
import logging
from progress.bar import IncrementalBar
from urllib.parse import urlparse
from page_loader import save
from page_loader import resources


def download(url, output):
    tags = ['img', 'link', 'script']
    obj = urlparse(url)
    hostname = f'{obj.scheme}://{obj.hostname}'
    new_url = re.sub("[^A-Za-z]", "-", url.split("//")[-1])
    path_to_html = os.path.join(output, f'{new_url}.html')
    path_to_files = os.path.join(output, f'{new_url}_files')
    try:
        get_html = requests.get(url)
        get_html.raise_for_status()
        logging.info(f'successful response from {url}')
        temp_html = get_html.text
        with IncrementalBar("Downloading:",
                            suffix='%(percent).1f%% - %(eta)ds\n',
                            max=3) as bar:
            for tag in tags:
                temp_html = resources.download(temp_html,
                                               path_to_files,
                                               hostname,
                                               tag)
                bar.next()
        return save.save(temp_html, path_to_html)
    except (requests.exceptions.HTTPError, ConnectionError) as e:
        logging.debug(e, e.__class__, e.__traceback__)
        logging.warning(f"Unsuccessful response from {url}")
