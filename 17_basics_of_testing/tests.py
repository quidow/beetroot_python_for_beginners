import phonebook
import unittest
from unittest.mock import patch
import io


class TestPhonebook(unittest.TestCase):

    def test_load_phonebook(self):
        self.assertIsInstance(phonebook.load_phonebook("test.json"), list)
        self.assertIsInstance(phonebook.load_phonebook(), list)

    def test_save_phonebook(self):
        phonebook.save_phonebook("test.json", [1, 2, 3])
        self.assertEqual(phonebook.load_phonebook("test.json"), [1, 2, 3])

    def test_search_entries(self):
        array = [{1: 1}, {2: 2}, {3: 3}]
        self.assertEqual(phonebook.search_entries(array, 2, 2), [1])

    def test_add_or_edit_entry(self):
        user_input = [
            'aaa',
            'bbb',
            'ccc',
            'ddd',
            'eee',
            'fff',
            'ggg'
        ]
        with patch('builtins.input', side_effect=user_input):
            new_entry = phonebook.add_or_edit_entry([])
        self.assertEqual(new_entry, {'first_name': 'aaa',
                                     'last_name': 'bbb',
                                     'full_name': 'aaa bbb',
                                     'telephone': 'ccc',
                                     'state': 'ddd',
                                     'city': 'eee'})
        user_input = [
            'ggg',
            'fff',
            'eee',
            'ddd',
            'ccc',
            'bbb',
            'aaa'
        ]
        with patch('builtins.input', side_effect=user_input):
            new_entry = phonebook.add_or_edit_entry([new_entry], 0)
        self.assertEqual(new_entry, {'first_name': 'ggg',
                                     'last_name': 'fff',
                                     'full_name': 'ggg fff',
                                     'telephone': 'eee',
                                     'state': 'ddd',
                                     'city': 'ccc'})

    def test_print_entries(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            phonebook.print_entries([{1: 1}, {2: 2}, {3: 3}], [1, 2])
        self.assertEqual(fake_stdout.getvalue(), "         2 2\n         3 3\n")
        with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            phonebook.print_entries([{1: 1}, {2: 2}, {3: 3}], [])
        self.assertEqual(fake_stdout.getvalue(), "No entry found\n")


if __name__ == '__main__':
    unittest.main()
