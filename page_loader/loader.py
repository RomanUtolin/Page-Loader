import os
import re


def download(url, output=os.getcwd()):
    if url.startswith('https://'):
        url = url[8:]
    elif url.startswith('http://'):
        url = url[7:]
    url = re.sub("[^A-Za-z]", "-", url) + '.html'
    return f'{output}/{url}'
