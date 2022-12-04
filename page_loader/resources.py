import os
import requests
import logging
from page_loader import save
from page_loader import names


def download(soup, path, hostname, tag):
    tags = {'img': 'src',
            'link': 'href',
            'script': 'src'}
    if not os.path.isdir(path):
        logging.info(f'Create directory : {path}')
        os.mkdir(path)
    tags_link = soup.find_all(tag)
    for tag_ in tags_link:
        if tag_.has_attr(tags[tag]):
            link = tag_[tags[tag]]
            if (link.startswith('http') and not link.startswith(hostname)) \
                    or link.startswith('//'):
                continue
            link = names.link(link, hostname)
            file_ = names.file(link, hostname)
            path_to_link = f'{path}/{file_}'
            try:
                get_link = requests.get(link)
                get_link.raise_for_status()
                link_data = get_link.content
                save.save(link_data, path_to_link)
                tag_[tags[tag]] = f'{path.split("/")[-1]}/{file_}'
            except (requests.exceptions.HTTPError,
                    ConnectionError,
                    OSError) as e:
                debug_info = (e, e.__class__, e.__traceback__)
                logging.debug(debug_info)
                logging.warning(
                    f"{link} wasn't downloaded")

    return soup
