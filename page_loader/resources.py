import os
import requests
import logging
import re
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
            if (link.startswith('http') and not link.startswith(hostname)) \
                    or link.startswith('//'):
                continue
            else:
                if link.startswith(hostname):
                    link = link
                elif not link.startswith('/'):
                    link = f'{hostname}/{link}'
                else:
                    link = f'{hostname}{link}'
                to_file =\
                    f'{re.sub("[^A-Za-z]", "-", hostname.split("//")[-1])}' \
                    f'-{"-".join(link.split("/")[3:])}'
                path_to_link = f'{path_to_files}/{to_file}'
                try:
                    get_link = requests.get(link)
                    get_link.raise_for_status()
                    if tag == 'img':
                        link_data = get_link.content
                    else:
                        link_data = get_link.text
                    save.save(link_data, path_to_link)
                    t[tags_link[tag]] =\
                        f'{path_to_files.split("/")[-1]}/{to_file}'
                except (requests.exceptions.HTTPError,
                        ConnectionError,
                        OSError) as e:
                    debug_info = (e, e.__class__, e.__traceback__)
                    logging.debug(debug_info)
                    logging.warning(
                        f"{link} wasn't downloaded")

    return soup.prettify()
