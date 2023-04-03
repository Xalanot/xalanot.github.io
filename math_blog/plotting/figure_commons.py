import logging
import matplotlib.pyplot as plt
from typing import Optional


def enable_comic_style():
  logging.getLogger('matplotlib.font_manager').disabled = True
  plt.xkcd(scale=1, length=100, randomness=2)


def create_figure() -> tuple[plt.Figure, plt.Axes]:
  return plt.subplots(1, 1)


def set_coordinate_boundaries(axis: plt.Axes, x_min: Optional[float], x_max: Optional[float], y_min: Optional[float], y_max: Optional[float]):
  axis.set_xlim(xmin=x_min, xmax=x_max)
  axis.set_ylim(ymin=y_min, ymax=y_max)


def add_coordinate_axis(axis: plt.Axes):
  axis.spines['left'].set_position('zero')
  axis.spines['right'].set_color('none')
  axis.spines['bottom'].set_position('zero')
  axis.spines['top'].set_color('none')

  axis.spines['left'].set_zorder(0)
  axis.spines['bottom'].set_zorder(0)


def turn_off_axis_markers(axis: plt.Axes):
  axis.set_xticks([])
  axis.set_yticks([])
