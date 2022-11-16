import os
import requests
from bs4 import BeautifulSoup


def download(html, path_to_files, domain):
    html = BeautifulSoup(html, 'html.parser')
    if not os.path.isdir(path_to_files):
        os.mkdir(path_to_files)
    list_link = html.find_all('link')
    list_script = html.find_all('script')
    for href in list_link:
        link = href['href']
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
                href['href'] = path_to_link
    for script in list_script:
        if script.has_attr('src'):
            link = script['src']
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
                    script['src'] = path_to_link

    return html.prettify()
