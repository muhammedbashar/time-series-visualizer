import unittest
import matplotlib as mpl
import time_series_visualizer as ts


class LinePlotTestCase(unittest.TestCase):
    def test_line_plot(self):
        fig = ts.draw_line_plot()
        self.assertIsInstance(fig, mpl.figure.Figure)


class BarPlotTestCase(unittest.TestCase):
    def test_bar_plot(self):
        fig = ts.draw_bar_plot()
        self.assertIsInstance(fig, mpl.figure.Figure)


class BoxPlotTestCase(unittest.TestCase):
    def test_box_plot(self):
        fig = ts.draw_box_plot()
        self.assertIsInstance(fig, mpl.figure.Figure)


if __name__ == "__main__":
    unittest.main()
