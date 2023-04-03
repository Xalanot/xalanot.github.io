from typing import Optional, Callable

import matplotlib.pyplot as plt
import numpy as np


def draw_point(axis: plt.Axes, x: float, y: float, color: Optional[str] = None, size: float = 10):
    axis.plot(x, y, marker="o", markersize=size, markerfacecolor=color, markeredgecolor="black")


def annotate_point(axis: plt.Axes, xy: tuple[float, float], xy_text: tuple[float, float], text: str, arrow_width: Optional[int] = None):
    axis.annotate(text=text, xy=xy, xytext=xy_text, arrowprops={"arrowstyle": "simple", "shrinkA": 2, "shrinkB": 10, "relpos": (0.5, 0.5), "mutation_scale": arrow_width})


def draw_function(axis: plt.Axes, function: Callable, x_min: float, x_max: float):
    x_range = np.linspace(x_min, x_max, 100, endpoint=True)
    axis.plot(x_range, function(x_range), color="black")
