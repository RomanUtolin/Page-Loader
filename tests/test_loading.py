import os
import tempfile
import pytest

from page_loader.loading import download


@pytest.fixture
def mock(requests_mock):
    return requests_mock.get('http://test.com/dir/test', text='test')


def test_loading(mock):
    with tempfile.TemporaryDirectory() as tmp:
        test_dir = download('http://test.com/dir/test', tmp)
        right_dir = os.path.join(tmp, 'test-com-dir-test.html')
        assert test_dir == right_dir


def test_parser(mock):
    with tempfile.TemporaryDirectory() as tmp:
        with open(download('http://test.com/dir/test', tmp)) as file:
            assert file.read().strip() == 'test'
