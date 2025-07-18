# test_artificialmasterpiecegeneratorstudionext.py
"""
Tests for ArtificialMasterpieceGeneratorStudioNext module.
"""

import unittest
from artificialmasterpiecegeneratorstudionext import ArtificialMasterpieceGeneratorStudioNext

class TestArtificialMasterpieceGeneratorStudioNext(unittest.TestCase):
    """Test cases for ArtificialMasterpieceGeneratorStudioNext class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ArtificialMasterpieceGeneratorStudioNext()
        self.assertIsInstance(instance, ArtificialMasterpieceGeneratorStudioNext)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ArtificialMasterpieceGeneratorStudioNext()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
