import re


def url(url_):
    new_url = re.sub("[^A-Za-z]", "-", url_.split("//")[-1])
    return new_url


def link(link_, hostname):
    if link_.startswith(hostname):
        pass
    elif not link_.startswith('/'):
        link_ = f'{hostname}/{link_}'
    else:
        link_ = f'{hostname}{link_}'
    return link_


def file(url_, hostname):
    name = f'{url(hostname)}-{"-".join(url_.split("/")[3:])}'
    if '.' not in name:
        name = f"{name}.html"
    return name
