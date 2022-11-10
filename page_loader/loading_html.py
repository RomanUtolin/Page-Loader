def download(html, path):
    with open(path, 'w') as file:
        file.write(html)
    return path
