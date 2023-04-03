from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import typer

from math_blog.plotting.figure_commons import enable_comic_style, create_figure, set_coordinate_boundaries, add_coordinate_axis, turn_off_axis_markers
from math_blog.plotting.draw_commons import draw_point, annotate_point, draw_function
from math_blog.plotting.io import save_figure


SCRIPT_PATH = Path(__file__)
OUTPUT_FOLDER = SCRIPT_PATH.parent.parent / "media"


def draw_single_point():
  enable_comic_style()
  fig, axis = create_figure()
  add_coordinate_axis(axis=axis)
  draw_point(axis, 0, 0.4, size=15)
  annotate_point(axis, (0, 0.4), (0.1, 0.4), text="f(0)=1", arrow_width=25)
  set_coordinate_boundaries(axis, x_min=-0.5, x_max=0.5, y_min=-0.2, y_max=0.8)
  turn_off_axis_markers(axis=axis)
  save_figure(fig, OUTPUT_FOLDER / "single_point.png")


def draw_negative_derivative():
  enable_comic_style()
  fig, axis = create_figure()
  add_coordinate_axis(axis=axis)
  point_x = 0
  point_y = 0.4
  draw_point(axis, point_x, point_y, size=15)
  draw_function(axis, lambda x: point_y - x, -0.4, 0.4)
  annotate_point(axis, (point_x, point_y), (point_x + 0.1, point_y), text="f'(0) < 0", arrow_width=25)
  set_coordinate_boundaries(axis, x_min=-0.5, x_max=0.5, y_min=-0.2, y_max=0.8)
  turn_off_axis_markers(axis=axis)
  save_figure(fig, OUTPUT_FOLDER / "negative_derivative.png")


def draw_zero_derivative():
  enable_comic_style()
  fig, axis = create_figure()
  add_coordinate_axis(axis=axis)
  point_x = 0
  point_y = 0.4
  draw_point(axis, point_x, point_y, size=15)
  draw_function(axis, lambda x: point_y + x*0, -0.4, 0.4)
  annotate_point(axis, (point_x, point_y), (point_x + 0.1, point_y + 0.2), text="f'(0) = 0", arrow_width=25)
  set_coordinate_boundaries(axis, x_min=-0.5, x_max=0.5, y_min=-0.2, y_max=0.8)
  turn_off_axis_markers(axis=axis)
  save_figure(fig, OUTPUT_FOLDER / "zero_derivative.png")


def draw_positive_derivative():
  enable_comic_style()
  fig, axis = create_figure()
  add_coordinate_axis(axis=axis)
  point_x = 0
  point_y = 0.4
  draw_point(axis, point_x, point_y, size=15)
  draw_function(axis, lambda x: point_y + x, -0.4, 0.4)
  annotate_point(axis, (point_x, point_y), (point_x + 0.1, point_y), text="f'(0) > 0", arrow_width=25)
  set_coordinate_boundaries(axis, x_min=-0.5, x_max=0.5, y_min=-0.2, y_max=0.8)
  turn_off_axis_markers(axis=axis)
  save_figure(fig, OUTPUT_FOLDER / "positive_derivative.png")


def draw_negative_second_derivative():
  enable_comic_style()
  fig, axis = create_figure()
  add_coordinate_axis(axis=axis)
  point_x = 0
  point_y = 0.4
  draw_point(axis, point_x, point_y, size=15)
  draw_function(axis, lambda x: point_y + np.log(x+ 1), -0.4, 0.4)
  annotate_point(axis, (point_x, point_y), (point_x + 0.1, point_y), text="f''(0) < 0", arrow_width=25)
  set_coordinate_boundaries(axis, x_min=-0.5, x_max=0.5, y_min=-0.2, y_max=0.8)
  turn_off_axis_markers(axis=axis)
  save_figure(fig, OUTPUT_FOLDER / "negative_second_derivative.png")


def draw_zero_second_derivative():
  enable_comic_style()
  fig, axis = create_figure()
  add_coordinate_axis(axis=axis)
  point_x = 0
  point_y = 0.4
  draw_point(axis, point_x, point_y, size=15)
  draw_function(axis, lambda x: point_y + x, -0.4, 0.4)
  annotate_point(axis, (point_x, point_y), (point_x + 0.1, point_y), text="f''(0) = 0", arrow_width=25)
  set_coordinate_boundaries(axis, x_min=-0.5, x_max=0.5, y_min=-0.2, y_max=0.8)
  turn_off_axis_markers(axis=axis)
  save_figure(fig, OUTPUT_FOLDER / "zero_second_derivative.png")


def draw_positive_second_derivative():
  enable_comic_style()
  fig, axis = create_figure()
  add_coordinate_axis(axis=axis)
  point_x = 0
  point_y = 0.4
  draw_point(axis, point_x, point_y, size=15)
  draw_function(axis, lambda x: point_y + np.exp(x) - 1, -0.4, 0.4)
  annotate_point(axis, (point_x, point_y), (point_x + 0.1, point_y), text="f''(0) > 0", arrow_width=25)
  set_coordinate_boundaries(axis, x_min=-0.5, x_max=0.5, y_min=-0.2, y_max=0.8)
  turn_off_axis_markers(axis=axis)
  save_figure(fig, OUTPUT_FOLDER / "positive_second_derivative.png")


def main():
  draw_single_point()
  draw_negative_derivative()
  draw_zero_derivative()
  draw_positive_derivative()
  draw_negative_second_derivative()
  draw_zero_second_derivative()
  draw_positive_second_derivative()
  

if __name__ == "__main__":
  typer.run(main)