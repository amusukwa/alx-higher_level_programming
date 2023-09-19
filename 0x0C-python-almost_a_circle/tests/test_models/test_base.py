import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    
    def test_constructor_with_id(self):
        b = Base(42)
        self.assertEqual(b.id, 42)

    def test_constructor_without_id(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)

    # Add more test cases for other methods as needed

if __name__ == '__main__':
    unittest.main()
