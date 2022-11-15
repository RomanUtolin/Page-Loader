import re
import os
import requests
from page_loader import loading_img
from page_loader import loading_html
from page_loader import loading_resources


def download(url, output):
    domain = ('/'.join(url.split("/")[:3]))
    new_url = re.sub("[^A-Za-z]", "-", url.split("//")[-1])
    path_to_html = os.path.join(output, f'{new_url}.html')
    path_to_files = os.path.join(output, f'{new_url}_files')
    html = requests.get(url)
    loading_resources.download(html, path_to_files, domain)
    html = loading_img.download(html, path_to_files, domain)
    return loading_html.download(html, path_to_html)
