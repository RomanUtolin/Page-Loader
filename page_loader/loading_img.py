import os
import requests
from bs4 import BeautifulSoup


def download(html, path_to_html):
    html = html.text
    path_img = os.path.join(os.path.splitext(path_to_html)[0] + '_files')
    if not os.path.isdir(path_img):
        os.mkdir(path_img)
    soup = BeautifulSoup(html, 'html.parser')
    list_img = soup.find_all('img')
    for img in list_img:
        if img.has_attr('src'):
            link = img['src']
            path_to_file = os.path.join(path_img, link.split("/")[-1])
            img_data = requests.get(link).content
            with open(path_to_file, 'wb') as f:
                f.write(img_data)
            img['src'] = path_to_file
    return soup.prettify()
