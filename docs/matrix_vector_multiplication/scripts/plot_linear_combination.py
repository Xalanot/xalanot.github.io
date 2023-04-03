import manim
import typer


class MatrixVectorMultiplicationLinearCombination(manim.Scene):
    def construct(self):
        matrix = manim.Matrix([[1, 3], [1, 5]])
        self.add(matrix)
