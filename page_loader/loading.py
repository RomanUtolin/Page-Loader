import os
import requests
import logging
import sys
from bs4 import BeautifulSoup
from progress.bar import IncrementalBar
from urllib.parse import urlparse
from page_loader import save
from page_loader import resources
from page_loader import names
from selenium import webdriver
import time


# def download(url, output):
#     tags = ['img', 'link', 'script']
#     obj = urlparse(url)
#     hostname = f'{obj.scheme}://{obj.hostname}'
#     new_url = names.url(url)
#     path_to_html = os.path.join(output, f'{new_url}.html')
#     path_to_files = os.path.join(output, f'{new_url}_files')
#     try:
#         headers = {
#             "cookie": "admin_jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhaWQiOjEsImlwIjoiMTkyLjE2OC40MC4yNDgiLCJleHAiOiIyMDI1LTA4LTI3VDIxOjQyOjAzLjE2MTI4NDIyMSswMzowMCIsImlzcyI6IndlYmFkbWluIiwibmJmIjoiMjAyNS0wOC0yN1QwOTo0MjowMi4xNjEyODQ5MTcrMDM6MDAiLCJpYXQiOiIyMDI1LTA4LTI3VDA5OjQyOjAyLjE2MTI4NDk5KzAzOjAwIn0.Qn_tu6uZvW-gz96ad7iQqncO_oL1pD_pBXaT0BB29KA; jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhaWQiOjEsInVubSI6InJvbWFuLnV0b2xpbiIsImxpcCI6IjE5Mi4xNjguNDAuMjQ4IiwiZ3JzIjpbMF0sImV4cCI6MTc1NjI3NzUyNywiaXNzIjoid2ViY29udHJvbCIsInYiOjF9.8J2IRzG4Kg2nnQpH6HN-BY1eJFvjkskoRBTU4nIys-0; jwtr=0198ea43-2d2c-7a6d-a969-d9c0bf1742ea"
#         }
#         get_html = requests.get(url, headers=headers)
#         get_html.raise_for_status()
#         logging.info(f'successful response from {url}')
#         temp_html = get_html.text
#         soup = BeautifulSoup(temp_html, 'html.parser')
#         with IncrementalBar("Downloading:",
#                             suffix='%(percent).1f%% - %(eta)ds\n',
#                             max=3) as bar:
#             for tag in tags:
#                 temp_html = resources.download(soup,
#                                                path_to_files,
#                                                hostname,
#                                                tag)
#                 bar.next()
#         return save.save(temp_html.prettify(), path_to_html)
#     except (requests.exceptions.HTTPError, ConnectionError) as e:
#         logging.debug(e, e.__class__, e.__traceback__)
#         logging.warning(f"Unsuccessful response from {url}")
#         sys.exit(1)


def download(url, output):
    tags = ['img', 'link', 'script']
    obj = urlparse(url)
    hostname = f'{obj.scheme}://{obj.hostname}'
    new_url = names.url(url)
    path_to_html = os.path.join(output, f'{new_url}.html')
    path_to_files = os.path.join(output, f'{new_url}_files')
    try:
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        logging.info('start webdriver')
        driver = webdriver.Chrome(options=options)
        logging.info(f'start req {url}')
        driver.get(url)
        logging.info('sleep')
        time.sleep(10)  # подождать загрузки JS
        html = driver.page_source
        logging.info(f'successful response from {url}')
        soup = BeautifulSoup(html, 'html.parser')
        with IncrementalBar("Downloading:",
                            suffix='%(percent).1f%% - %(eta)ds\n',
                            max=3) as bar:
            for tag in tags:
                temp_html = resources.download(soup,
                                               path_to_files,
                                               hostname,
                                               tag)
                bar.next()
        return save.save(temp_html.prettify(), path_to_html)
    except (requests.exceptions.HTTPError, ConnectionError) as e:
        logging.debug(e, e.__class__, e.__traceback__)
        logging.warning(f"Unsuccessful response from {url}")
        sys.exit(1)
