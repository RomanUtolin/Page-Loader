import os
import requests
from bs4 import BeautifulSoup


def download(html, path_to_files, domain):
    html = html.text
    if not os.path.isdir(path_to_files):
        os.mkdir(path_to_files)
    soup = BeautifulSoup(html, 'html.parser')
    list_link = soup.find_all('link')
    list_script = soup.find_all('script')
    for link in list_link:
        print(link['href'])
    for script in list_script:
        if script.has_attr('src'):
            print('script')
