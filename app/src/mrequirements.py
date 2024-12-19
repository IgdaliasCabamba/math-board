import requests
import os
import pathlib
from .static_files import *

root_path = os.environ["IMATH_ROOT_PATH"]

DATAS = {
    "https://unpkg.com/mathlive/dist/mathlive.min.js":os.path.join(root_path, "static", "packages", "mathlive.min.js"),
}

STATIC_DATA = {
    HTML:os.path.join(root_path, "templates", "index.html"),
    CSS:os.path.join(root_path, "static", "mstyle.css")
}

def touch(file):
    folder = pathlib.Path(file).parent
    if not os.path.exists(folder):
        os.makedirs(folder)
    pathlib.Path(file).touch()

def download(url):
    return requests.get(url, allow_redirects=True)

def save(content, name_with_path):
    touch(name_with_path)
    with open(name_with_path, 'wb') as fp:
        fp.write(content)

def main():
    for url, path in DATAS.items():
        if os.path.exists(path):
            continue
        else:
            resp = download(url)
            save(resp.content, path)
    
    for file, path in STATIC_DATA.items():
        if not os.path.exists(path):
            touch(path)
            with open(path, 'w') as fp:
                fp.write(file)

if __name__ == "__main__":
    main()