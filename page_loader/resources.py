import os
import requests
from bs4 import BeautifulSoup


def download(html, path_to_files, hostname, tag):
    tags_link = {'img': 'src',
                 'link': 'href',
                 'script': 'src'}
    soup = BeautifulSoup(html, 'html.parser')
    if not os.path.isdir(path_to_files):
        os.mkdir(path_to_files)
    tags = soup.find_all(tag)
    for t in tags:
        if t.has_attr(tags_link[tag]):
            link = t[tags_link[tag]]
            if link.startswith('http') or link.startswith('//'):
                continue
            else:
                if not link.startswith('/'):
                    link = f'/{link}'
                link = f'{hostname}{link}'
                path_to_link = f'{path_to_files}/{link.split("/")[-1]}'
                link_data = requests.get(link).content
                with open(path_to_link, 'wb') as f:
                    f.write(link_data)
                t[tags_link[tag]] = path_to_link

    return soup.prettify()
