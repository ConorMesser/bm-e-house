from PIL import Image
import turtle as t
import matplotlib.testing.compare as mpcompare
import unittest
import tempfile
import os.path
import inspect

import draw_house

#NM notes: TestShapes is inheriting from parent class unittest.TestCase 
class TestShapes(unittest.TestCase):
    def _compare_canvas_to_expected(self, expected_filename):
        ''' compares the current canvas to an expected filename.
        Returns None if and only if the files are identical'''
        TOLERANCE = 1.0 # somewhere between 0 and 255, higher is more lax.
        with tempfile.TemporaryDirectory() as tmp_dirname:
            calling_function = inspect.stack()[1][3]

            actual_ps = os.path.join(tmp_dirname, '%s.ps' % calling_function)
            actual_png = os.path.join(tmp_dirname, '%s.png' % calling_function)
            canvas = t.getcanvas()
            canvas.postscript(file=actual_ps)
            with Image.open(actual_ps) as im:
                im.save(actual_png)

            return mpcompare.compare_images(expected_filename, actual_png, TOLERANCE)

    def setUp(self):
        t.clearscreen()
        screen = t.Screen()
        screen.clear()
        screen.setup(900, 700)
        screen.screensize(900, 700)
        t.hideturtle()
        self._turtle = t.Turtle()
        self._turtle.hideturtle()

    def test_rect(self):
        # test if a rectangle gets produced at the same location and with same size as test rectangle
        draw_house.draw_rect(self._turtle, 20, 20, 40, 40)
        self.assertIsNone(self._compare_canvas_to_expected(expected_filename='./nm_test_data/test_rect.png'))

    def test_rect_fail(self):
        # test that a badly sized rectangle fails to compare as equal to the correctly positioned/sized rectangle
        draw_house.draw_rect(self._turtle, 20, 20, 60,60)
        self.assertIsNotNone(self._compare_canvas_to_expected(expected_filename='./nm_test_data/test_rect.png'))

    def test_line(self):
        # test if angled line looks same as reference image
        draw_house.draw_single_line(self._turtle, 0, 0, 100, 90)
        self.assertIsNone(self._compare_canvas_to_expected(expected_filename='./nm_test_data/test_line.png'))

    def test_full_scene(self):
        # test if house produced looks same as expected image (created earlier)
        draw_house.draw_house(900, 700, keep_window_open=False)
        self.assertIsNone(self._compare_canvas_to_expected(expected_filename='./nm_test_data/test_full_scene.png'))


if __name__ == '__main__':
    unittest.main()
