import re
import os
import requests
from page_loader import html
from page_loader import resources


def download(url, output):
    tags = [('img', 'src'), ('link', 'href'), ('script', 'src')]
    new_url = re.sub("[^A-Za-z]", "-", url.split("//")[-1])
    domain = ('/'.join(url.split("/")[:3]))
    path_to_html = os.path.join(output, f'{new_url}.html')
    path_to_files = os.path.join(output, f'{new_url}_files')
    get_html = requests.get(url).text
    for tag in tags:
        temp_html = resources.download(get_html, path_to_files, domain, tag)

    return html.download(temp_html, path_to_html)
