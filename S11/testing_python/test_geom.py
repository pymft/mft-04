import geom
import unittest


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rectangle = geom.Rectangle(2.0, 5.0)

    def test_get_area(self):
        self.assertEqual(self.rectangle.area, 10.0)

    def test_get_perimeter(self):
        self.assertEqual(self.rectangle.perimeter, 14.0)

    def test_set_new_area(self):
        self.rectangle.area = 40.0
        self.assertEqual(self.rectangle.width, 4.0)
        self.assertEqual(self.rectangle.height, 10.0)

    def test_set_non_numerical_value_area(self):
        with self.assertRaises(TypeError):
            self.rectangle.area = 'salam'

    def test_set_non_numerical_value_perimeter(self):
        with self.assertRaises(TypeError):
            self.rectangle.perimeter = 'salam'

