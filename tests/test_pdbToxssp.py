from unittest import TestCase
import unittest

from DSSPparser import pdbToxssp


class TestPdbToxssp(TestCase):
    def test_pdbToxssp(self):
        # self.fail()
        result = pdbToxssp('2GW9')
        self.assertIsNotNone(result)


if __name__ == "__main__":
    unittest.main(verbosity=2)
