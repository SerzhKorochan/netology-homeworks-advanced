import pytest
from src.yandex_api import create_folder, get_current_datetime


class TestYandexApi:
    @pytest.mark.parametrize('folder_name, expected_value', [
        (get_current_datetime(), 201),
        ('NewFolder', 409)
    ])
    def test_successfully_creating_folder(self, folder_name, expected_value):
        assert create_folder(folder_name) == expected_value
