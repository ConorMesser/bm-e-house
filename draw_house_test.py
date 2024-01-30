from PIL import Image
import turtle as t
import matplotlib.testing.compare as mpcompare
import unittest
import tempfile
import os.path

import draw_house

#NM notes: TestShapes is inheriting from parent class unittest.TestCase 
class TestShapes(unittest.TestCase):
    def _compare_canvas_to_expected(self, expected_filename):
        ''' compares the current canvas to an expected filename.
        Returns None if and only if the files are identical'''
        TOLERANCE = 1.0 # somewhere between 0 and 255, higher is more lax.
        with tempfile.TemporaryDirectory() as tmp_dirname:
            actual_ps = os.path.join(tmp_dirname, 'canvas.ps')
            actual_png = os.path.join(tmp_dirname, 'canvas.png')
            canvas = t.getcanvas()
            canvas.postscript(file=actual_ps)
            with Image.open(actual_ps) as im:
                im.save(actual_png)

            return mpcompare.compare_images(expected_filename, actual_png, TOLERANCE)

    def setUp(self):
        t.reset()
        t.screensize(500, 500)
        t.hideturtle()
        self._turtle = t.Turtle()
        self._turtle.hideturtle()

    def test_rect(self):
        draw_house.draw_rect(self._turtle, 20, 20, 40, 40)
        self.assertIsNone(self._compare_canvas_to_expected(expected_filename='./nm_test_data/test_rect.png'))

    def test_rect_fail(self):
        # test that a badly sized circle fails to compare as equal
        draw_house.draw_rect(self._turtle, 20, 20, 60,60)
        self.assertIsNotNone(self._compare_canvas_to_expected(expected_filename='./nm_test_data/test_rect.png'))

    def test_line(self):
        draw_house.draw_single_line(self._turtle, 0, 0, 100, 45)
        self.assertIsNotNone(self._compare_canvas_to_expected(expected_filename='./nm_test_data/test_line.png'))

    def test_only_house(self):
        pass

    def test_full_scene(self):
        draw_house.draw_house()
        self.assertIsNone(self._compare_canvas_to_expected(expected_filename='./nm_test_data/test_house.png'))


if __name__ == '__main__':
    unittest.main()


