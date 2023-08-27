import unittest
from src.phonebook import Phonebook


class TestPhonebook(unittest.TestCase):

    def test_add_for_hashtag(self):
        # setup
        phonebook = Phonebook()
        expected_return = "Nome invalido"
        name = "#marcello"
        phone = "123456"
        # test
        add_fail = phonebook.add(name, phone)
        # expected
        self.assertEqual(add_fail, expected_return)

    def test_add_for_arroba(self):
        # setup
        phonebook = Phonebook()
        expected_return = "Nome invalido"
        name = "@marcello"
        phone = "123456"
        # test
        add_fail = phonebook.add(name, phone)
        # expected
        self.assertEqual(add_fail, expected_return)

    def test_add_for_exclamation_point(self):
        # setup
        phonebook = Phonebook()
        expected_return = "Nome invalido"
        name = "!marcello"
        phone = "123456"
        # test
        add_fail = phonebook.add(name, phone)
        # expected
        self.assertEqual(add_fail, expected_return)

    def test_add_for_cifrao(self):
        # setup
        phonebook = Phonebook()
        expected_return = "Nome invalido"
        name = "$marcello"
        phone = "123456"
        # test
        add_fail = phonebook.add(name, phone)
        # expected
        self.assertEqual(add_fail, expected_return)

    def test_add_for_percentage(self):
        # setup
        phonebook = Phonebook()
        expected_return = "Nome invalido"
        name = "%marcello"
        phone = "123456"
        # test
        add_fail = phonebook.add(name, phone)
        # expected
        self.assertEqual(add_fail, expected_return)

    def test_add_for_empty_phone(self):
        # setup
        phonebook = Phonebook()
        expected_return = "Numero invalido"
        name = "marcello"
        phone = ""
        # test
        add_fail = phonebook.add(name, phone)
        # expected
        self.assertEqual(add_fail, expected_return)

    def test_add_ok(self):
        # setup
        phonebook = Phonebook()
        expected_return = "Numero adicionado"
        name = "marcello"
        phone = "123456"
        # test
        add_success = phonebook.add(name, phone)
        # expected
        self.assertEqual(add_success, expected_return)

    def test_look_up_with_hashtag(self):
        # setup
        phonebook = Phonebook()
        name = "#marcello"
        expected_return = "Nome invalido"
        # test
        lookup_fail = phonebook.lookup(name)
        # expected
        self.assertEqual(lookup_fail, expected_return)

    def test_look_up_with_arroba(self):
        # setup
        phonebook = Phonebook()
        name = "@marcello"
        expected_return = "Nome invalido"
        # test
        lookup_fail = phonebook.lookup(name)
        # expected
        self.assertEqual(lookup_fail, expected_return)

    def test_look_up_with_exclamation_point(self):
        # setup
        phonebook = Phonebook()
        name = "!marcello"
        expected_return = "Nome invalido"
        # test
        lookup_fail = phonebook.lookup(name)
        # expected
        self.assertEqual(lookup_fail, expected_return)

    def test_look_up_with_cifrao(self):
        # setup
        phonebook = Phonebook()
        name = "$marcello"
        expected_return = "Nome invalido"
        # test
        lookup_fail = phonebook.lookup(name)
        # expected
        self.assertEqual(lookup_fail, expected_return)

    def test_look_up_with_percentage(self):
        # setup
        phonebook = Phonebook()
        name = "%marcello"
        expected_return = "Nome invalido"
        # test
        lookup_fail = phonebook.lookup(name)
        # expected
        self.assertEqual(lookup_fail, expected_return)

    def test_look_up_ok(self):
        # setup
        phonebook = Phonebook()
        name = "marcello"
        phone = "123456"
        expected_return = phone
        # test
        phonebook.add(name, phone)
        lookup_success = phonebook.lookup(name)
        # expected
        self.assertEqual(lookup_success, expected_return)

    def test_get_names(self):
        # setup
        phonebook = Phonebook()
        expected_return = ["POLICIA"]
        # test
        get_names_success = phonebook.get_names()
        # expected
        self.assertEqual(get_names_success, expected_return)

    def test_get_numbers(self):
        # setup
        phonebook = Phonebook()
        expected_return = ["190"]
        # test
        get_numbers_success = phonebook.get_numbers()
        # expected
        self.assertEqual(get_numbers_success, expected_return)

    def test_clear(self):
        # setup
        phonebook = Phonebook()
        expected_return = "phonebook limpado"
        # test
        clear_success = phonebook.clear()
        # expected
        self.assertEqual(clear_success, expected_return)

    def test_search(self):
        # setup
        phonebook = Phonebook()
        search_name = "POLICIA"
        expected_return = [("POLICIA", "190")]
        # test
        search_success = phonebook.search(search_name)
        # expected
        self.assertEqual(search_success, expected_return)

    def test_get_phonebook_sorted(self):
        # setup
        phonebook = Phonebook()
        name1 = "Marcello"
        phone1 = "1234"
        name2 = "Tatu"
        phone2 = "5667"
        expected_return = [("Marcello", "1234"), ("POLICIA", "190"), ("Tatu", "5667")]
        # test
        phonebook.add(name1, phone1)
        phonebook.add(name2, phone2)
        get_phonebook_sorted_success = phonebook.get_phonebook_sorted()
        # expected
        self.assertEqual(get_phonebook_sorted_success, expected_return)

    def test_get_phonebook_reverse(self):
        # setup
        phonebook = Phonebook()
        name1 = "Marcello"
        phone1 = "1234"
        name2 = "Tatu"
        phone2 = "5667"
        expected_return = [("Tatu", "5667"), ("POLICIA", "190"), ("Marcello", "1234")]
        # test
        phonebook.add(name1, phone1)
        phonebook.add(name2, phone2)
        get_phonebook_sorted_success = phonebook.get_phonebook_reverse()
        # expected
        self.assertEqual(get_phonebook_sorted_success, expected_return)

    def test_delete(self):
        # setup
        phonebook = Phonebook()
        name = "POLICIA"
        expected_return = "Numero deletado"
        # test
        delete_success = phonebook.delete(name)
        # expected
        self.assertEqual(delete_success, expected_return)

    def test_change_number(self):
        # setup
        phonebook = Phonebook()
        name = "POLICIA"
        new_number = "191"
        expected_return = "Numero modificado"
        # test
        modify_success = phonebook.change_number(name, new_number)
        # expected
        self.assertEqual(modify_success, expected_return)

    def test_change_number_error(self):
        # setup
        phonebook = Phonebook()
        name = "POLICIAaa"
        new_number = "191"
        expected_return = "Nome não encontrado"
        # test
        modify_success = phonebook.change_number(name, new_number)
        # expected
        self.assertEqual(modify_success, expected_return)

    def test_get_name_by_number(self):
        # setup
        phonebook = Phonebook()
        number = "190"
        expected_return = "POLICIA"
        # test
        get_name_by_number_success = phonebook.get_name_by_number(number)
        # expected
        self.assertEqual(get_name_by_number_success, expected_return)

    def test_get_name_by_number_error(self):
        # setup
        phonebook = Phonebook()
        number = "1910"
        expected_return = "Número não encontrado"
        # test
        get_name_by_number_error = phonebook.get_name_by_number(number)
        # expected
        self.assertEqual(get_name_by_number_error, expected_return)
