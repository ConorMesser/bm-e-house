from PIL import Image
import turtle
import matplotlib.testing.compare as mpcompare
import unittest
import draw_house
import tempfile
import os.path


#NM notes: TestShapes is inheriting from parent class unittest.TestCase 
class TestShapes(unittest.TestCase):
    def _compare_canvas_to_expected(self, expected_filename):
        ''' compares the current canvas to an expected filename.
        Returns None if and only if the files are identical'''
        TOLERANCE = 1.0 # somewhere between 0 and 255, higher is more lax.
        with tempfile.TemporaryDirectory() as tmp_dirname:
            actual_ps = os.path.join(tmp_dirname, 'canvas.ps')
            actual_png = os.path.join(tmp_dirname, 'canvas.png')
            canvas = turtle.getcanvas()
            canvas.postscript(file=actual_ps)
            with Image.open(actual_ps) as im:
                im.save(actual_png)
            return mpcompare.compare_images(expected_filename, actual_png, TOLERANCE)


    def setUp(self):
        turtle.reset()

    def test_rect(self):
        t = turtle.getturtle()
        draw_house.draw_rect(t, 20, 20, 40, 40)
        t.hideturtle()
        self.assertIsNone(self._compare_canvas_to_expected(expected_filename='~/nm_test_data/test_rect.png'))

    def test_rect_fail(self):
        # test that a badly sized circle fails to compare as equal
        t = turtle.getturtle()
        draw_house.draw_rect(t, 20, 20, 60,60)
        t.hideturtle()
        self.assertIsNotNone(self._compare_canvas_to_expected(expected_filename='~/nm_test_data/test_rect.png'))

    def test_house(self):
        draw_house()
        self.assertIsNone(self._compare_canvas_to_expected(expected_filename='~/nm_test_data/test_house.png'))



if __name__ == '__main__':
    unittest.main()


