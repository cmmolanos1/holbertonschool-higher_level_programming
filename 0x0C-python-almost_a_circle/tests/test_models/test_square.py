#!/usr/bin/python3

"""
Unittest for models/square.py
"""

import sys
import os
import unittest
import io
import contextlib
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class SquareTest(unittest.TestCase):
    """Tests for square class."""

    def test_class_docstring(self):
        """Tests for the presence of a class docstring"""
        self.assertTrue(len(Square.__doc__) >= 1)

    def setUp(self):
        Base._Base__nb_objects = 0

    def tearDown(self):
        if os.path.exists("Base.json"):
            os.remove("Base.json")
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_one_arg(self):
        s = Square(5)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)
        self.assertEqual(s.x, 0)
        self.assertEqual(s.y, 0)

    def test_two_args(self):
        r1 = Square(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 10)
        self.assertEqual(r1.x, 2)
        self.assertEqual(r1.y, 0)

    def test_three_args(self):
        r2 = Square(98, 12, 64)
        self.assertEqual(r2.id, 1)
        self.assertEqual(r2.width, 98)
        self.assertEqual(r2.height, 98)
        self.assertEqual(r2.x, 12)
        self.assertEqual(r2.y, 64)

    def test_four_args(self):
        r3 = Square(4, 51, 96, 88)
        self.assertEqual(r3.id, 88)
        self.assertEqual(r3.width, 4)
        self.assertEqual(r3.height, 4)
        self.assertEqual(r3.x, 51)
        self.assertEqual(r3.y, 96)

    def test_5args(self):
        pass

    def test_private_attributes(self):
        r5 = Square(11, 6, 87, 6)
        d = {"_Rectangle__width": 11, "_Rectangle__height": 11,
             "_Rectangle__x": 6, "_Rectangle__y": 87, "id": 6}
        self.assertEqual(r5.__dict__, d)

    def test_none(self):
        with self.assertRaises(TypeError) as x:
            r = Square(None)
        self.assertEqual(
            "width must be an integer",
            str(x.exception))

    def test_no_args(self):
        with self.assertRaises(TypeError) as x:
            r = Square()
        self.assertEqual(
            "__init__() missing 1 required positional argument: 'size'",
            str(x.exception))

    def test_string_test(self):
        with self.assertRaises(TypeError) as x:
            r = Square(10, "2")
        self.assertEqual(
            "x must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Square("10", 2)
        self.assertEqual(
            "width must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Square(10, 2, "3")
        self.assertEqual(
            "y must be an integer",
            str(x.exception))
        r = Square(10, 2, 0, "lol")
        self.assertEqual(r.id, "lol")

    def test_float_test(self):
        with self.assertRaises(TypeError) as x:
            r = Square(10, 2.1)
        self.assertEqual(
            "x must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Square(9.0, 2)
        self.assertEqual(
            "width must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Square(10, 2, 3.2131)
        self.assertEqual(
            "y must be an integer",
            str(x.exception))
        r = Square(10, 2, 0, 12.3)
        self.assertEqual(r.id, 12.3)

    def test_list_test(self):
        with self.assertRaises(TypeError) as x:
            r = Square(10, [])
        self.assertEqual(
            "x must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Square([1, 2, 3], 2)
        self.assertEqual(
            "width must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Square(10, 2, [[2, 4]])
        self.assertEqual(
            "y must be an integer",
            str(x.exception))
        r = Square(10, 2, 0, ["hi"])
        self.assertEqual(r.id, ["hi"])

    def test_dict_test(self):
        with self.assertRaises(TypeError) as x:
            r = Square(10, {})
        self.assertEqual(
            "x must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Square({"a": 1, "b": 2, "c": 3}, 2)
        self.assertEqual(
            "width must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Square(10, 2, {"a": 1})
        self.assertEqual(
            "y must be an integer",
            str(x.exception))
        r = Square(10, 2, 0, {"hi": None})
        self.assertEqual(r.id, {"hi": None})

    def test_bool_test(self):
        with self.assertRaises(TypeError) as x:
            r = Square(10, True)
        self.assertEqual(
            "x must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Square(False, 2)
        self.assertEqual(
            "width must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Square(10, 2, True)
        self.assertEqual(
            "y must be an integer",
            str(x.exception))
        r = Square(10, 2, 0, False)
        self.assertEqual(r.id, False)

    def test_tuple_test(self):
        with self.assertRaises(TypeError) as x:
            r = Square(10, ())
        self.assertEqual(
            "x must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Square((1, 2, 3), 2)
        self.assertEqual(
            "width must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Square(10, 2, (2, 4))
        self.assertEqual(
            "y must be an integer",
            str(x.exception))
        r = Square(10, 2, 0, ("hi",))
        self.assertEqual(r.id, ("hi",))

    def test_sets_test(self):
        with self.assertRaises(TypeError) as x:
            r = Square(10, {})
        self.assertEqual(
            "x must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Square({1, 2, 3}, 2)
        self.assertEqual(
            "width must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r = Square(10, 2, {2, 4})
        self.assertEqual(
            "y must be an integer",
            str(x.exception))
        r = Square(10, 2, 0, {"hi"})
        self.assertEqual(r.id, {"hi"})

    def test_negative_ints(self):
        with self.assertRaises(ValueError) as x:
            r = Square(1, -2)
        self.assertEqual(
            "x must be >= 0",
            str(x.exception))
        with self.assertRaises(ValueError) as x:
            r = Square(-1, -2)
        self.assertEqual(
            "width must be > 0",
            str(x.exception))
        with self.assertRaises(ValueError) as x:
            r = Square(1, 2, -1)
        self.assertEqual(
            "y must be >= 0",
            str(x.exception))
        r = Square(1, 2, 5, -1)
        self.assertEqual(r.id, -1)

    def test_zero(self):
        r = Square(6, 0)
        self.assertEqual(r.x, 0)
        with self.assertRaises(ValueError) as x:
            r = Square(0, 2)
        self.assertEqual(
            "width must be > 0",
            str(x.exception))
        r = Square(1, 0, 0, 0)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertEqual(r.id, 0)

    def test_area(self):
        r = Square(3, 2)
        self.assertEqual(r.area(), 9)
        r = Square(1, 20, 1)
        self.assertEqual(r.area(), 1)
        r = Square(4, 5, 6, 2)
        self.assertEqual(r.area(), 16)
        r = Square(9, 7, 4, 6)
        self.assertEqual(r.area(), 81)

    def test_display(self):
        s = Square(2)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            s.display()
        s = f.getvalue()
        output = "##\n##\n"
        self.assertEqual(s, output)
        s = Square(2, 4)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            s.display()
        s = f.getvalue()
        output = "    ##\n    ##\n"
        self.assertEqual(s, output)

    def test_str(self):
        r = Square(4, 6, 2, 1)
        self.assertEqual(r.__str__(), "[Square] (1) 6/2 - 4")
        r = Square(1, 1, 0)
        self.assertEqual(r.__str__(), "[Square] (1) 1/0 - 1")
        r = Square(1, 1)
        self.assertEqual(r.__str__(), "[Square] (2) 1/0 - 1")

    def test_display_with_coords(self):
        s = Square(2, 3, 2, 2)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            s.display()
        s = f.getvalue()
        output = "\n\n   ##\n   ##\n"
        self.assertEqual(s, output)
        s = Square(1, 0, 1)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            s.display()
        s = f.getvalue()
        output = "\n#\n"
        self.assertEqual(s, output)
        s = Square(2)
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            s.display()
        s = f.getvalue()
        output = "##\n##\n"
        self.assertEqual(s, output)

    def test_args_and_kwargs(self):
        r = Square(1, 2, 3, 4)
        r.update(99, height=66)
        self.assertEqual(r.__str__(), "[Square] (99) 2/3 - 1")

    def test_invalid_kwargs(self):
        r = Square(1, 2, 3, 4)
        r.update(weight=25)
        self.assertEqual(hasattr(r, 'weight'), False)

    def test_size(self):
        r = Square(5)
        self.assertEqual(r.size, 5)
        r.size = 25
        self.assertEqual(r.size, 25)
        with self.assertRaises(TypeError) as x:
            r.size = "hello"
        self.assertEqual(
            "width must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r.size = [1, 2]
        self.assertEqual(
            "width must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r.size = (2,)
        self.assertEqual(
            "width must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r.size = {"a": 1}
        self.assertEqual(
            "width must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r.size = True
        self.assertEqual(
            "width must be an integer",
            str(x.exception))
        with self.assertRaises(TypeError) as x:
            r.size = {1, 2}
        self.assertEqual(
            "width must be an integer",
            str(x.exception))

    def test_to_dictionary(self):
        r = Square(10, 2, 1, 9)
        r_d = {'x': 2, 'size': 10, 'y': 1, 'id': 9}
        self.assertEqual(r.to_dictionary(), r_d)
        self.assertEqual(r.to_dictionary() is r_d, False)
        r = Square(9, 4, 15)
        r_d = {'x': 4, 'id': 1, 'y': 15, 'size': 9}
        self.assertEqual(r.to_dictionary(), r_d)
        self.assertEqual(r.to_dictionary() is r_d, False)
        r = Square(62, 414)
        r_d = {'x': 414, 'id': 2, 'y': 0, 'size': 62}
        self.assertEqual(r.to_dictionary(), r_d)
        self.assertEqual(r.to_dictionary() is r_d, False)

    def test_to_json_string(self):
        r = Square(10, 7, 2)
        d = r.to_dictionary()
        json_d = Base.to_json_string([d])
        self.assertEqual(type(json_d), str)
        self.assertEqual(d, {'id': 1, 'x': 7, 'y': 2, 'size': 10})

    def test_save_to_file(self):
        r1 = Square(10, 7, 2)
        r2 = Square(2, 4)
        Square.save_to_file([r1, r2])
        res = '[{"x": 7, "y": 2, "size": 10, "id": 1},' + \
              ' {"x": 4, "y": 0, "size": 2, "id": 2}]'
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), len(res))

    def test_from_json_string(self):
        list_input = [{'id': 89, 'size': 10},
                      {'id': 7, 'size': 7}]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        l = [{'size': 10, 'id': 89}, {'size': 7, 'id': 7}]
        self.assertEqual(list_output, l)

    def test_create(self):
        s1 = Square(3, 5, 1)
        s1_dictionary = s1.to_dictionary()
        s2 = Square.create(**s1_dictionary)
        self.assertEqual((s1 == s2), False)
        self.assertEqual((s1 is s2), False)

    def test_load_from_files(self):
        square_list = Square.load_from_file()
        self.assertEqual(square_list, [])

    def test_save_to_file_None(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual(len(file.read()), 2)

    def test_save_to_file_empty_list(self):
        Square.save_to_file([])
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), '[]')
        empty = []
        Square.save_to_file(empty)
        with open("Square.json", "r") as file:
            self.assertEqual(file.read(), '[]')

    def test_save_to_file_two_args(self):
        with self.assertRaises(TypeError):
            Square.save_to_file([], 6)

if __name__ == '__main__':
    unittest.main()
