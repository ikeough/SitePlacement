import os
import sys
import unittest
sys.path.append("../SitePlacement")
from SitePlacement import sitePlacement

class TestSitePlacement(unittest.TestCase):
    def test_site_placement(self):
        result = sitePlacement()
        self.assertIsNotNone(result['model'])
        self.assertIsNotNone(result['computed']['floors'])
        self.assertIsNotNone(result['computed']['area'])

if __name__ == 'main__':
    unittest.main()