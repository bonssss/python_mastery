import unittest
from cube import area_cube, volume_cube

class Testcube(unittest.TestCase):
    def setUp(self):
        """Set up a Cube instance for testing."""
        self.side_length = 3
    def test_area_cube(self):
        """Test the area of the cube."""
        expected_area = 6 * (self.side_length ** 2)
        self.assertEqual(area_cube(self.side_length), expected_area)
        print(f"Area of cube with side length {self.side_length}: {area_cube(self.side_length)}")
    
    def test_volume_cube(self):
        """Test the volume of the cube."""
        expected_volume = self.side_length ** 3
        self.assertEqual(volume_cube(self.side_length), expected_volume)
        print()
        
        print(f"Volume of cube with side length {self.side_length}: {volume_cube(self.side_length)}")
        
if __name__ == '__main__':
    unittest.main()