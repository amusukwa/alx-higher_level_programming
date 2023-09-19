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

    def test_to_json_string(self):
        class Temp(Base):
            def to_dictionary(self):
                return {"id": self.id}

        b1 = Temp(1)
        b2 = Temp(2)
        json_str = Temp.to_json_string([b1.to_dictionary(), b2.to_dictionary()])
        expected = '[{"id": 1}, {"id": 2}]'
        self.assertEqual(json_str, expected)
    
    def test_to_json_string_with_list(self):
        class Temp(Base):
            def to_dictionary(self):
                return {"id": self.id}

        b1 = Temp(12)
        json_str = Base.to_json_string([b1.to_dictionary()])
        expected = '[{"id": 12}]'
        self.assertEqual(json_str, expected)

    def test_from_json_string_with_none(self):
        json_list = Base.from_json_string(None)
        self.assertEqual(json_list, [])

    def test_from_json_string_with_valid_json(self):
        json_str = '[{"id": 89}]'
        json_list = Base.from_json_string(json_str)
        self.assertEqual(json_list, [{"id": 89}])       
        
        

    # Add more test cases for other methods as needed


if __name__ == '__main__':
    unittest.main()
