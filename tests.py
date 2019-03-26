import unittest

from rectangles_intersection import Rectangle, intersect_section, intersect_rectangles


class TestRectangle(unittest.TestCase):
    def test_rectangle_correct(self):
        rect1 = Rectangle(0, 0, 2, 2)
        self.assertTrue(rect1.is_correct)

        rect2 = Rectangle(0, 0, 0, 0)
        self.assertTrue(rect2.is_correct)

    def test_rectangle_incorrect(self):
        rect1 = Rectangle(2, 2, 0, 0)
        self.assertFalse(rect1.is_correct)

        rect2 = Rectangle(2, 2, 0, 3)
        self.assertFalse(rect2.is_correct)

        rect3 = Rectangle(2, 2, 3, 0)
        self.assertFalse(rect3.is_correct)


class TestIntersectSection(unittest.TestCase):
    def test_sections_incorrect_should_raise(self):
        with self.assertRaises(ValueError):
            intersect_section(2, 0, 2, 0)

        with self.assertRaises(ValueError):
            intersect_section(2, 0, 0, 0)

        with self.assertRaises(ValueError):
            intersect_section(0, 0, 2, 0)

    def test_sections_empty_intersection(self):
        self.assertIsNone(intersect_section(0, 1, 2, 3))
        self.assertIsNone(intersect_section(2, 3, 0, 1))
        self.assertIsNone(intersect_section(0, 0, 1, 1))

    def test_sections_correct_intersection(self):
        # -1  0  1  2  3  4
        #     |_____|
        #        |_____|
        self.assertEqual(intersect_section(0, 2, 1, 3), (1, 2))
        self.assertEqual(intersect_section(1, 3, 0, 2), (1, 2))

        # -1  0  1  2  3  4
        #        |__|
        #     |________|
        self.assertEqual(intersect_section(0, 3, 1, 2), (1, 2))
        self.assertEqual(intersect_section(1, 2, 0, 3), (1, 2))

        # -1  0  1  2  3  4
        #        |
        #     |________|
        self.assertEqual(intersect_section(0, 3, 1, 1), (1, 1))
        self.assertEqual(intersect_section(1, 1, 0, 3), (1, 1))

        # -1  0  1  2  3  4
        #     |
        #     |________|
        self.assertEqual(intersect_section(0, 3, 0, 0), (0, 0))
        self.assertEqual(intersect_section(0, 0, 0, 3), (0, 0))

        # -1  0  1  2  3  4
        #              |
        #     |________|
        self.assertEqual(intersect_section(0, 3, 3, 3), (3, 3))
        self.assertEqual(intersect_section(3, 3, 0, 3), (3, 3))

        # Самопересечение
        # -1  0  1  2  3  4
        #     |________|
        #     |________|
        self.assertEqual(intersect_section(0, 3, 0, 3), (0, 3))


class TestIntersectRectangles(unittest.TestCase):
    def test_intersect_rectangles_should_raise(self):
        with self.assertRaises(ValueError):
            intersect_rectangles(
                Rectangle(2, 2, 0, 0),
                Rectangle(2, 2, 0, 0),
            )

        with self.assertRaises(ValueError):
            intersect_rectangles(
                Rectangle(1, 1, 2, 2),
                Rectangle(2, 2, 0, 0),
            )

        with self.assertRaises(ValueError):
            intersect_rectangles(
                Rectangle(2, 2, 0, 0),
                Rectangle(1, 1, 2, 2),
            )

    def test_intersect_rectangles_empty_intersection(self):
        self.assertIsNone(intersect_rectangles(
            Rectangle(0, 0, 1, 1),
            Rectangle(2, 2, 3, 3),
        ))

        self.assertIsNone(intersect_rectangles(
            Rectangle(2, 2, 3, 3),
            Rectangle(0, 0, 1, 1),
        ))

    def test_intersect_rectangles_correct_intersection(self):
        #  4
        #  3     _____
        #  2  __|__   |
        #  1 |  |__|__|
        #  0 |_____|
        #    0  1  2  3  4
        self.assertEqual(
            intersect_rectangles(
                Rectangle(0, 0, 2, 2),
                Rectangle(1, 1, 3, 3),
            ),
            Rectangle(1, 1, 2, 2)
        )
        self.assertEqual(
            intersect_rectangles(
                Rectangle(1, 1, 3, 3),
                Rectangle(0, 0, 2, 2),
            ),
            Rectangle(1, 1, 2, 2)
        )

        #  4
        #  3  _____
        #  2 |   __|__
        #  1 |__|__|  |
        #  0    |_____|
        #    0  1  2  3  4
        self.assertEqual(
            intersect_rectangles(
                Rectangle(0, 1, 2, 3),
                Rectangle(1, 0, 3, 2),
            ),
            Rectangle(1, 1, 2, 2)
        )
        self.assertEqual(
            intersect_rectangles(
                Rectangle(1, 0, 3, 2),
                Rectangle(0, 1, 2, 3),
            ),
            Rectangle(1, 1, 2, 2)
        )

        #  4
        #  3  ________
        #  2 |        |
        #  1 |  *     |
        #  0 |________|
        #    0  1  2  3  4
        self.assertEqual(
            intersect_rectangles(
                Rectangle(1, 1, 1, 1),
                Rectangle(0, 0, 2, 2),
            ),
            Rectangle(1, 1, 1, 1)
        )

        #  4
        #  3  ________
        #  2 |   __   |
        #  1 |  |__|  |
        #  0 |________|
        #    0  1  2  3  4
        self.assertEqual(
            intersect_rectangles(
                Rectangle(0, 0, 3, 3),
                Rectangle(1, 1, 2, 2),
            ),
            Rectangle(1, 1, 2, 2)
        )
        self.assertEqual(
            intersect_rectangles(
                Rectangle(1, 1, 2, 2),
                Rectangle(0, 0, 3, 3),
            ),
            Rectangle(1, 1, 2, 2)
        )

        # Самопересечение
        self.assertEqual(
            intersect_rectangles(
                Rectangle(0, 0, 1, 1),
                Rectangle(0, 0, 1, 1),
            ),
            Rectangle(0, 0, 1, 1)
        )

