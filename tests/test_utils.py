from unittest import TestCase
from registrypol.policy import RegistryPolicy
from registrypol.utils import dump, load


class TestUtils(TestCase):
    def test_dump(self):
        pass

    def test_load(self):
        with open('tests/files/registry.pol', 'rb') as file:
            self.assertIsInstance(load(file), RegistryPolicy)
