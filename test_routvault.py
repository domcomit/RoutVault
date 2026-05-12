# test_routvault.py
"""
Tests for RoutVault module.
"""

import unittest
from routvault import RoutVault

class TestRoutVault(unittest.TestCase):
    """Test cases for RoutVault class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = RoutVault()
        self.assertIsInstance(instance, RoutVault)
        
    def test_run_method(self):
        """Test the run method."""
        instance = RoutVault()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
