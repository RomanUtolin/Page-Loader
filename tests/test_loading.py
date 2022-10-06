import os
import tempfile
from page_loader.loading import download


def test_loading():
    with tempfile.TemporaryDirectory() as tmp:
        test_dir = download('https://ru.hexlet.io/courses', tmp)
        right_dir = os.path.join(tmp, 'ru-hexlet-io-courses.html')
        assert test_dir == right_dir


def test_parser():
    with tempfile.TemporaryDirectory() as tmp:
        with open(download('http://seclub.org', tmp)) as f:
            test_file = f.read()
        with open("./tests/fixtures/right.html") as f:
            right = f.read()
        assert test_file == right
