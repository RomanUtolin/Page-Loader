import re
import requests
import os


def download(url, output):
    req = requests.get(url)
    site_text = req.text
    if url.startswith('https://'):
        url = url[8:]
    elif url.startswith('http://'):
        url = url[7:]
    new_url = re.sub("[^A-Za-z]", "-", url) + '.html'
    path = os.path.join(output, new_url)
    with open(path, 'w') as file:
        file.write(site_text)
    return path
