import os
import requests
from bs4 import BeautifulSoup


def download(html, path_to_files, domain):
    html = html.text
    if not os.path.isdir(path_to_files):
        os.mkdir(path_to_files)
    soup = BeautifulSoup(html, 'html.parser')
    list_img = soup.find_all('img')
    for img in list_img:
        link = img['src']
        if link.startswith('http'):
            continue
        else:
            if not link.startswith('/'):
                link = f'/{link}'
            link = f'{domain}{link}'
            path_to_img = f'{path_to_files}/{link.split("/")[-1]}'
            img_data = requests.get(link).content
            with open(path_to_img, 'wb') as f:
                f.write(img_data)
            img['src'] = path_to_img

    return soup.prettify()
