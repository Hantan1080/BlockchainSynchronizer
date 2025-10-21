# test_blockchainsynchronizer.py
"""
Tests for BlockchainSynchronizer module.
"""

import unittest
from blockchainsynchronizer import BlockchainSynchronizer

class TestBlockchainSynchronizer(unittest.TestCase):
    """Test cases for BlockchainSynchronizer class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockchainSynchronizer()
        self.assertIsInstance(instance, BlockchainSynchronizer)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockchainSynchronizer()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
