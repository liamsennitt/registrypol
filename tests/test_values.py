from unittest import TestCase
from registrypol.values import RegistryValue


class TestRegistryValue(TestCase):
    def test_valid_key(self):
        value = RegistryValue(key='', value='', type=1, size=1, data=b'\x00')
        self.assertEqual(value.key, '')

    def test_invalid_key_type(self):
        with self.assertRaises(TypeError):
            RegistryValue(key=None, value='', type=1, size=1, data=b'\x00')

    def test_valid_value(self):
        value = RegistryValue(key='', value='', type=1, size=1, data=b'\x00')
        self.assertEqual(value.value, '')

    def test_invalid_value_type(self):
        with self.assertRaises(TypeError):
            RegistryValue(key='', value=None, type=1, size=1, data=b'\x00')

    def test_valid_type(self):
        value = RegistryValue(key='', value='', type=1, size=1, data=b'\x00')
        self.assertEqual(value.type, 1)

    def test_valid_type_str_reg_none(self):
        value = RegistryValue(key='', value='', type='REG_NONE', size=1, data=b'\x00')
        self.assertEqual(value.type, 0)

    def test_valid_type_str_reg_sz(self):
        value = RegistryValue(key='', value='', type='REG_SZ', size=1, data=b'\x00')
        self.assertEqual(value.type, 1)

    def test_valid_type_str_reg_expand_sz(self):
        value = RegistryValue(key='', value='', type='REG_EXPAND_SZ', size=1, data=b'\x00')
        self.assertEqual(value.type, 2)

    def test_valid_type_str_reg_binary(self):
        value = RegistryValue(key='', value='', type='REG_BINARY', size=1, data=b'\x00')
        self.assertEqual(value.type, 3)

    def test_valid_type_str_reg_dword(self):
        value = RegistryValue(key='', value='', type='REG_DWORD', size=1, data=b'\x00')
        self.assertEqual(value.type, 4)

    def test_valid_type_str_reg_dword_little_endian(self):
        value = RegistryValue(key='', value='', type='REG_DWORD_LITTLE_ENDIAN', size=1, data=b'\x00')
        self.assertEqual(value.type, 4)

    def test_valid_type_str_reg_dword_big_endian(self):
        value = RegistryValue(key='', value='', type='REG_DWORD_BIG_ENDIAN', size=1, data=b'\x00')
        self.assertEqual(value.type, 5)

    def test_valid_type_str_reg_link(self):
        value = RegistryValue(key='', value='', type='REG_LINK', size=1, data=b'\x00')
        self.assertEqual(value.type, 6)

    def test_valid_type_str_reg_multi_sz(self):
        value = RegistryValue(key='', value='', type='REG_MULTI_SZ', size=1, data=b'\x00')
        self.assertEqual(value.type, 7)

    def test_valid_type_str_reg_qword(self):
        value = RegistryValue(key='', value='', type='REG_QWORD', size=1, data=b'\x00')
        self.assertEqual(value.type, 11)

    def test_valid_type_str_reg_qword_little_endian(self):
        value = RegistryValue(key='', value='', type='REG_QWORD_LITTLE_ENDIAN', size=1, data=b'\x00')
        self.assertEqual(value.type, 11)

    def test_invalid_type_type(self):
        with self.assertRaises(TypeError):
            RegistryValue(key='', value='', type=None, size=1, data=b'\x00')

    def test_valid_size(self):
        value = RegistryValue(key='', value='', type=1, size=1, data=b'\x00')
        self.assertEqual(value.size, 1)

    def test_invalid_size_type(self):
        with self.assertRaises(TypeError):
            RegistryValue(key='', value='', type=1, size=None, data=b'\x00')

    def test_valid_data(self):
        value = RegistryValue(key='', value='', type=1, size=1, data=b'\x00')
        self.assertEqual(value.data, b'\x00')

    def test_invalid_data_type(self):
        with self.assertRaises(TypeError):
            RegistryValue(key='', value='', type=1, size=1, data=None)
