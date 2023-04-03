import manim
import numpy as np

from math_blog.functions.sinus import sinus_taylor


class SinusTaylorAtZero(manim.Scene):
    def construct(self):
        axes = np.Axes(
            x_range=[-np.pi, np.pi, np.pi / 2],
            y_range=[-1.5, 1.5, 1.0],
            tips=False,
            axis_config={"include_numbers": True, "decimal_number_config": {"num_decimal_places": 2}},
        )
        sin_graph = axes.plot(lambda x: np.sin(x))
        self.add(axes, sin_graph)

        taylor_graph = axes.plot(lambda x: sinus_taylor(x, 0, 0), color="red")
        taylor_text = manim.Text("n=0", color="red").to_edge(manim.UR)
        self.add(taylor_graph, taylor_text)
        self.wait()
        for n in [1, 3, 5, 7, 9]:
            new_taylor_graph = axes.plot(lambda x: sinus_taylor(x, 0, n), color="red")
            self.play(manim.ReplacementTransform(taylor_graph, new_taylor_graph))
            self.wait(0.1)
            taylor_graph = new_taylor_graph
            new_taylor_text = manim.Text(f"n={n}", color="red").to_edge(manim.UR)
            self.remove(taylor_text)
            self.add(new_taylor_text)
            taylor_text = new_taylor_text
            self.wait()


class SinusTaylorAtZeroDifference(manim.Scene):
    def construct(self):
        axes = manim.Axes(
            x_range=[0, np.pi, np.pi / 4],
            y_range=[-5, 1, 1],
            tips=False,
            axis_config={"include_numbers": True},
            x_axis_config={"decimal_number_config": {"num_decimal_places": 2}},
            y_axis_config={"scaling": manim.LogBase(custom_labels=True)},
        )
        self.add(axes)

        difference_graph = axes.plot(lambda x: np.abs(np.sin(x) - sinus_taylor(x, 0, 0)), color="red", x_range=[0.01, np.pi])
        difference_text = manim.Text("n=0", color="red").to_edge(manim.UR)
        self.add(difference_graph, difference_text)
        self.wait()
        for n in [1, 3, 5, 7, 9]:
            new_difference_graph = axes.plot(lambda x: np.abs(np.sin(x) - sinus_taylor(x, 0, n)), color="red", x_range=[0.03, np.pi])
            self.play(manim.ReplacementTransform(difference_graph, new_difference_graph))
            self.wait(0.1)
            difference_graph = new_difference_graph
            new_difference_text = manim.Text(f"n={n}", color="red").to_edge(manim.UR)
            self.remove(difference_text)
            self.add(new_difference_text)
            difference_text = new_difference_text
            self.wait()


class SinusTaylorAtDifferentPoints(manim.Scene):
    def construct(self):
        graph_axes = manim.Axes(
            x_range=[-np.pi, 2*np.pi, np.pi / 2],
            y_range=[-1.5, 1.5, 1.0],
            x_length=6,
            y_length=5,
            tips=False,
            y_axis_config={"include_numbers": True, "decimal_number_config": {"num_decimal_places": 2}},
        )
        graph_x_axis = graph_axes.get_x_axis()
        graph_x_axis.add_labels({
            -3.14: "$-\\pi$",
            -1.57: "$-\\frac{\\pi}{2}$",
            1.57: "$\\frac{\\pi}{2}$",
            3.14: "$\\pi$",
            4.71: "$\\frac{3\\pi}{2}$",
            6.28: "$2\\pi$"
        })
        graph_axes.center()
        graph_axes.shift(manim.DOWN)
        graph_title = manim.Text("Taylor approximation of sinus (n=3)", font_size=25)
        graph_title.next_to(graph_axes, direction=5 * manim.UP)
        sin_graph = graph_axes.plot(lambda x: np.sin(x))

        t = manim.ValueTracker(0)
        graph_initial_point = [graph_axes.coords_to_point(t.get_value(), np.sin(t.get_value()))]
        graph_dot = manim.Dot(point=graph_initial_point, color="red")
        graph_dot.add_updater(lambda x: x.move_to(graph_axes.c2p(t.get_value(), np.sin(t.get_value()))))
        taylor_graph = graph_axes.plot(lambda x: sinus_taylor(x, t.get_value(), 3), color="red")
        taylor_graph.add_updater(lambda m: m.become(graph_axes.plot(lambda x: sinus_taylor(x, t.get_value(), 3), color="red")))
        
        first_plot = manim.VGroup(graph_axes, graph_title, sin_graph, graph_dot, taylor_graph)
        first_plot.shift(3.5 * manim.LEFT)

        difference_axes = manim.Axes(
            x_range=[-np.pi, 2*np.pi, np.pi / 2],
            y_range=[-5, 1, 1],
            x_length=6,
            y_length=5,
            tips=False,
            x_axis_config={"decimal_number_config": {"num_decimal_places": 2}},
            y_axis_config={"scaling": manim.LogBase(custom_labels=True), "include_numbers": True},
        )
        difference_x_axis = difference_axes.get_x_axis()
        difference_x_axis.add_labels({
            -3.14: "$-\\pi$",
            -1.57: "$-\\frac{\\pi}{2}$",
            1.57: "$\\frac{\\pi}{2}$",
            3.14: "$\\pi$",
            4.71: "$\\frac{3\\pi}{2}$",
            6.28: "$2\\pi$"
        })
        difference_axes.center()
        difference_axes.shift(manim.DOWN)
        difference_axes.match_height(graph_axes)
        difference_title = manim.Text("Difference of taylor approximation and real sinus", font_size=25)
        difference_title.next_to(difference_axes, direction=5 * manim.UP)

        difference_initial_point = [difference_axes.coords_to_point(t.get_value(), 1e-5)]
        difference_dot = manim.Dot(point=difference_initial_point, color="red")
        difference_dot.add_updater(lambda x: x.move_to(difference_axes.c2p(t.get_value(), 1e-5)))
        difference_graph = difference_axes.plot(lambda x: np.abs(np.sin(x) - sinus_taylor(x, t.get_value(), 3)) + 1e-7, color="red", x_range=[-np.pi, 2*np.pi])
        difference_graph.add_updater(lambda m: m.become(difference_axes.plot(lambda x: np.abs(np.sin(x) - sinus_taylor(x, t.get_value(), 3)) + 1e-7, color="red", x_range=[-np.pi, 2*np.pi], use_smoothing=True)))

        second_plot = manim.VGroup(difference_axes, difference_title, difference_dot, difference_graph)
        second_plot.shift(3.5 * manim.RIGHT)
        
        self.add(first_plot)
        self.add(second_plot)
        self.play(t.animate.set_value(np.pi), run_time=5)
        self.wait()
