import unittest
from unittest.mock import patch
from parameterized import parameterized
import src.app as app


class TestBookkeeping(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    @parameterized.expand([['10006', True], ['10007', False]])
    def test_document_existence(self, doc_number, expected_value):
        self.assertEqual(app.check_document_existance(doc_number), expected_value)

    @patch('src.app.get_doc_owner_name', return_value=9)
    def test_get_owner_name(self, owner_name):
        self.assertEqual(owner_name(), 9)
        # TODO have to understand working of "mock"
