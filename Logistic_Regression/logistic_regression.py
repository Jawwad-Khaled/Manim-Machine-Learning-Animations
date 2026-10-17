from manim import *
import numpy as np

class Introduction(Scene):
    def construct(self):
        axes = Axes(x_range=[0, 10, 2], y_range=[0, 1.2, 0.2], x_length=9, y_length=6).shift(LEFT*1).add_coordinates()
        axis_labels = axes.get_axis_labels(x_label='\\text{Hours Studied}', y_label='\\text{Probability Of Passing}')
        linear_graph = axes.plot(lambda x: 0.12946611 * x, x_range=[0, 10], color=BLUE)
        logistic_graph = axes.plot(lambda x: 1 / (1 + np.exp(-(-2.03882363 + 0.81116393 * x))), x_range=[0, 10], color=BLUE)
        text1 = MathTex(r'y\in\{0, 1\}')
        text2 = Tex(r'Sigmoid function').shift(UP*2.5)
        text3 = Tex(r'General solution with gradient descent').shift(UP*1.25)
        text4 = Tex(r'Brief overview of previously covered topics')
        text5 = Tex(r'More on nonlinearity').shift(DOWN*1.25)
        text6 = Tex('Implementation using numpy').shift(DOWN*2.5)
        text7 = Tex('Finding partial derivatives').shift(UP*1)
        text8 = Tex('Finding critical points for multivariable functions')
        text9 = Tex('Some linear algebra').shift(DOWN*1)
        np.random.seed(75)
        x = 9 * np.random.rand(30)
        y = 6 * x + 40 + 10 * np.random.randn(30)
        y = [1 if item > 70 else 0 for item in y]
        dots = [Dot((axes.c2p(i, j)), color=YELLOW) for i, j in zip(x, y)]
        self.play(LaggedStart(Create(axes), Create(axis_labels)), run_time=5)   
        self.play(LaggedStart(*[Write(dot) for dot in dots], lag_ratio=0.25, run_time=3))
        self.wait()
        self.play(Create(linear_graph))
        self.wait()
        self.play(ReplacementTransform(linear_graph, logistic_graph))
        self.wait()
        self.play(Uncreate(axis_labels), Uncreate(axes), *[Unwrite(dot) for dot in dots], Uncreate(logistic_graph), run_time=3)
        self.play(Write(text1))
        self.wait()
        self.play(Unwrite(text1))
        self.play(LaggedStart(Write(text2), Write(text3), Write(text4), Write(text5), Write(text6), lag_ratio=0.95, run_time=10))
        self.wait()
        self.play(LaggedStart(Unwrite(text6), Unwrite(text5), Unwrite(text4), Unwrite(text3), Unwrite(text2), lag_ratio=0.95, run_time=5))
        self.play(LaggedStart(Write(text7), Write(text8), Write(text9), lag_ratio=0.95, run_time=10))
        self.wait()
        self.play(LaggedStart(Unwrite(text9), Unwrite(text8), Unwrite(text7), lag_ratio=0.95, run_time=5))
        self.wait()

class Three_Dimensional_Part_Of_Introduction(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(x_range=[0, 10, 1], y_range=[0, 10, 1], z_range=[0, 1, 0.2], x_length=5, y_length=5, z_length=5)
        graph = Surface(lambda u, v: axes.c2p(u, v, 1 / (1 + np.exp(-(-2.67651639 + 0.34427395 * u + 0.47943091 * v)))), u_range=[0, 10], v_range=[0, 10])
        graph_stuff = VGroup(axes, graph)
        graph_stuff.shift(ORIGIN - axes.c2p(0, 0, 0.35))
        np.random.seed(75)
        x = 9 * np.random.rand(30)
        y = 2 + 7 * np.random.rand(30)
        z = 4 * x + 2 * y + 40 + 10 * np.random.randn(30)
        z = np.clip(z, 0, 100)
        z = [1 if item > 70 else 0 for item in z]
        dots = [Dot3D((axes.c2p(i, j, k)), color=YELLOW) for i, j, k in zip(x, y, z)]
        self.set_camera_orientation(phi=75*DEGREES)
        self.add(graph_stuff, *[dot for dot in dots])
        self.begin_ambient_camera_rotation(rate=PI/10, about='theta')
        self.wait(20)
        self.stop_ambient_camera_rotation()