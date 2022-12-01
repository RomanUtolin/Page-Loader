import os
import requests
import logging
from bs4 import BeautifulSoup
from page_loader import save


def download(html, path_to_files, hostname, tag):
    tags_link = {'img': 'src',
                 'link': 'href',
                 'script': 'src'}
    soup = BeautifulSoup(html, 'html.parser')
    if not os.path.isdir(path_to_files):
        logging.info(f'Create directory : {path_to_files}')
        os.mkdir(path_to_files)
    tags = soup.find_all(tag)
    for t in tags:
        if t.has_attr(tags_link[tag]):
            link = t[tags_link[tag]]
            if link.startswith('https') or link.startswith('//'):
                continue
            else:
                if not link.startswith('/'):
                    link = f'/{link}'
                link = f'{hostname}{link}'
                path_to_link = f'{path_to_files}/{link.split("/")[-1]}'
                try:
                    get_link = requests.get(link)
                    get_link.raise_for_status()
                    link_data = get_link.content
                    save.save_file(link_data, path_to_link)
                    t[tags_link[tag]] = path_to_link
                except (requests.exceptions.HTTPError,
                        ConnectionError,
                        OSError) as e:
                    debug_info = (e, e.__class__, e.__traceback__)
                    logging.debug(debug_info)
                    logging.warning(
                        f"{link} wasn't downloaded")

    return soup.prettify()
