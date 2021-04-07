import unittest
from unittest.mock import patch
import src.app as app


class TestBookkeeping(unittest.TestCase):

    @patch('builtins.input', return_value='11-2')
    def test_get_existing_user(self, mock_input):
        self.assertEqual(app.get_doc_owner_name(), 'Геннадий Покемонов')

    @patch('builtins.input', return_value='100067')
    def test_get_non_existing_user(self, mock_input):
        self.assertEqual(app.get_doc_owner_name(), None)

    def test_quantity_of_names_of_docs(self):
        self.assertEqual(len(app.get_all_doc_owners_names()), len(app.documents))

    def test_show_doc_info(self):
        document = {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"}
        expected_value = 'passport "2207 876234" "Василий Гупкин"'
        self.assertEqual(app.show_document_info(document), expected_value)

    @patch('builtins.input', return_value='11-2')
    def test_shelf_num_by_doc(self, mock_input):
        self.assertEqual(app.get_doc_shelf(), '1')

    @patch('builtins.input', side_effect=['777', 'passport', 'Ivan Ivanov', '4'])
    def test_add_new_doc(self, mock_input):
        self.assertEqual(app.add_new_doc(), '4')

    @patch('builtins.input', return_value='10006')
    def test_delete_doc(self, mock_input):
        self.assertEqual(app.delete_doc(), ('10006', True))

    @patch('builtins.input', side_effect=['10006', '3'])
    def test_move_doc_to_shelf_3(self, mock_input):
        self.assertEqual(app.move_doc_to_shelf(), ('10006', '3'))

    @patch('builtins.input', return_value='10')
    def test_add_new_shelf(self, mock_input):
        self.assertEqual(app.add_new_shelf(), ('10', True))
