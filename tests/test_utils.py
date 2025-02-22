from src.utils import read_json, create_objects_from_json


def test_get_path_to_file(mock_read_json_file):
    data = mock_read_json_file("../data/products.json")
    assert len(data) == 2


def test_get_no_path():
    data = read_json("")
    assert data == []


def test_create_objects_from_json(data):
    result = create_objects_from_json(data)
    assert len(result) == 2
