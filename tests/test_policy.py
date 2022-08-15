from unittest import TestCase
from registrypol.values import RegistryValue
from registrypol.policy import RegistryPolicy


class TestRegistryPolicy(TestCase):
    def test_valid_values(self):
        policy = RegistryPolicy(values=[])
        self.assertEqual(policy.values, [])

    def test_invalid_values_type(self):
        with self.assertRaises(TypeError):
            RegistryPolicy(values=None)

    def test_valid_values_element(self):
        value = RegistryValue(key='', value='', type=1, size=1, data=b'\x00')
        policy = RegistryPolicy(values=[value])
        self.assertIsInstance(policy, RegistryPolicy)

    def test_invalid_rule_collections_element_type(self):
        with self.assertRaises(TypeError):
            RegistryPolicy(values=[None])
