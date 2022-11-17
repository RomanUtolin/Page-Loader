import os
import requests
from bs4 import BeautifulSoup


def download(html, path_to_files, domain, tag):
    soup = BeautifulSoup(html, 'html.parser')
    if not os.path.isdir(path_to_files):
        os.mkdir(path_to_files)
    tags = soup.find_all(tag[0])
    for t in tags:
        if t.has_attr(tag[1]):
            link = t[tag[1]]
            if link.startswith('http') or link.startswith('//'):
                continue
            else:
                if not link.startswith('/'):
                    link = f'/{link}'
                link = f'{domain}{link}'
                path_to_link = f'{path_to_files}/{link.split("/")[-1]}'
                link_data = requests.get(link).content
                with open(path_to_link, 'wb') as f:
                    f.write(link_data)
                t[tag[1]] = path_to_link

    return soup.prettify()
