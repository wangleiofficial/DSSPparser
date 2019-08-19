from unittest import TestCase
import unittest
from DSSPparser import parseDSSP
import os


class TestParseDSSP(TestCase):
    def setUp(self):
        self.parser = parseDSSP(os.path.join(os.path.dirname(__file__), 'data', '2GW9.dssp'))
        self.parser.parse()

    def test_getResnums(self):
        resnums = self.parser.getResnums
        self.assertIsNotNone(resnums)

    def test_getInsCode(self):
        inscode = self.parser.getInsCode
        self.assertIsInstance(inscode, list)

    def test_getChain(self):
        chain = self.parser.getChain
        self.assertIsInstance(chain, list)

    def test_getAAs(self):
        aa = self.parser.getAAs
        self.assertIsInstance(aa, list)

    def test_getSecStruc(self):
        secstruc = self.parser.getSecStruc
        self.assertIsInstance(secstruc, list)

    def test_getSecStrucDetail(self):
        secstrucDetail = self.parser.getSecStrucDetail
        self.assertIsInstance(secstrucDetail, list)


if __name__ == "__main__":
    unittest.main(verbosity=2)
