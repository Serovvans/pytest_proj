import pytest

from utils.dicts import get_val


@pytest.fixture
def base_dict():
    return {"vcs": "mercurial"}


@pytest.fixture()
def empty_dict():
    return dict()


def test_get_val(base_dict):
    assert get_val(base_dict, "vcs") == "mercurial"
    assert get_val(base_dict, "vcs", "git") == "mercurial"


def test_get_val_with_empty(empty_dict):
    assert get_val(empty_dict, "vcs", "git") == "git"
    assert get_val(empty_dict, "vcs", "bazaar") == "bazaar"
