import re
import os
import requests
from page_loader import loading_img
from page_loader import loading_html


def download(url, output):
    new_url = re.sub("[^A-Za-z]", "-", url.split("//")[-1]) + '.html'
    path_to_html = os.path.join(output, new_url)
    html = requests.get(url)
    html = loading_img.download(html, path_to_html)
    return loading_html.download(html, path_to_html)
