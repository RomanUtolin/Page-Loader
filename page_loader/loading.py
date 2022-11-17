import re
import os
import requests
from urllib.parse import urlparse
from page_loader import html
from page_loader import resources


def download(url, output):
    tags = [('img', 'src'), ('link', 'href'), ('script', 'src')]
    obj = urlparse(url)
    hostname = f'{obj.scheme}://{obj.hostname}'
    new_url = re.sub("[^A-Za-z]", "-", url.split("//")[-1])
    path_to_html = os.path.join(output, f'{new_url}.html')
    path_to_files = os.path.join(output, f'{new_url}_files')
    temp_html = requests.get(url).text
    for tag in tags:
        temp_html = resources.download(temp_html, path_to_files, hostname, tag)

    return html.download(temp_html, path_to_html)
