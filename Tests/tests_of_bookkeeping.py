import unittest
from unittest.mock import patch
import src.app as app


class TestBookkeeping(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    # @parameterized.expand([['10006', True], ['10007', False]])
    # def test_document_existence(self, doc_number, expected_value):
    #     self.assertEqual(app.check_document_existance(doc_number), expected_value)

    @patch('builtins.input', return_value='10006')
    def test_get_existing_user(self, mock_input):
        self.assertEqual(app.get_doc_owner_name(), 'Аристарх Павлов')

    @patch('builtins.input', return_value='100067')
    def test_get_non_existing_user(self, mock_input):
        self.assertEqual(app.get_doc_owner_name(), None)

    def test_quantity_of_names_of_docs(self):
        self.assertEqual(len(app.get_all_doc_owners_names()), len(app.documents))

    # @patch('builtins.print', return_value={"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"})
    # def test_show_doc_info(self):
    #     pass
