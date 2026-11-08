from manim import *
import numpy as np

class Introduction(Scene):
    def construct(self):
        table = Table([['Likes Chocolate Cake', 'Favorite Move', '...', 'Likes Soda', 'Favorite Ice Cream Flavor'],
            ['False', 'Endgame', '...', 'True', 'Vanilla'],
            ['True', 'The Matrix', '...', 'False', 'Butterscotch'],
            ['True', 'Troll 2', '...', 'True', 'Mint Chocolate Chip'],
            ['...', '...', '...', '...', '...'],
            ['True', 'Interstellar', '...', 'True', 'Chocolate'],
            ['True', 'Coco', '...', 'False', 'Butterscotch'],
            ['False', 'PAW Patrol: The Movie', '...', 'True', 'Strawberry']]).scale(0.4)
        text1 = Tex(r'You passed!').shift(UP*3)
        text2 = Tex(r'So you decide to buy ice cream to celebrate!').shift(UP*1)
        text3 = Tex(r'But you do not know which flavor to buy').shift(DOWN*1)
        text4 = Tex(r'So you survey your classmates!').shift(DOWN*3)
        text5 = Tex(r'Gradient boosting and XGboost require').shift(UP*2)
        text6 = Tex(r'a strong foundation in calculus').shift(UP*1.5)
        text7 = Tex(r'Single decision trees and random forests').shift(UP*0.25)
        text8 = Tex(r'require much less math').shift(DOWN*0.25)
        text9 = Tex(r'Linear algebra is not as important in this video').shift(DOWN*1.5)
        text10 = Tex(r'but it is still helpful to know').shift(DOWN*2)

        self.play(Write(text1))
        self.wait()
        self.play(Write(text2))
        self.wait()
        self.play(Write(text3))
        self.wait()
        self.play(Write(text4))
        self.wait()
        self.play(Unwrite(text1), Unwrite(text2), Unwrite(text3), Unwrite(text4))
        self.play(Write(table))        
        self.wait()
        self.play(Unwrite(table))
        self.play(LaggedStart(Write(text5), Write(text6), Write(text7), Write(text8), Write(text9), Write(text10), run_time=10, lag_ratio=0.8))
        self.wait()
        self.play(LaggedStart(Unwrite(text10), Unwrite(text9), Unwrite(text8), Unwrite(text7), Unwrite(text6), Unwrite(text5), run_time=5, lag_ratio=0.8))

class Parametric_And_Non_Parametric_Models(Scene):
    def construct(self):
        text1 = Tex('Parametric Models').shift(UP*2)
        text2 = MathTex(r'\text{10 data points }\rightarrow\text{ }\hat{y}=\beta_0+\beta_1x_1+\cdots+\beta_px_p')
        text3 = MathTex(r'\text{1000 data points }\rightarrow\text{ still }\hat{y}=\beta_0+\beta_1x_1+\cdots+\beta_px_p').shift(DOWN*2)
        text4 = Tex('Nonparametric Models').shift(UP*2)
        text5 = Tex('10 data points').shift(LEFT*3+UP*0.5)
        text6 = Tex('1000 data points').shift(RIGHT*3+UP*0.5)

        self.play(Write(text1), Write(text2), Write(text3))
        self.wait()
        self.play(Unwrite(text1), Unwrite(text2), Unwrite(text3))
        self.play(Write(text4), Write(text5), Write(text6))
        self.wait()
        self.play(Unwrite(text4), Unwrite(text5), Unwrite(text6))

class Separating_Data(Scene):
    def construct(self):
        tracker1 = ValueTracker(4)
        tracker2 = ValueTracker(0.5)
        axes = Axes(x_range=[0, 10, 2], y_range=[0, 1.2, 0.5], x_length=9, y_length=5).add_coordinates()
        axis_labels = axes.get_axis_labels(x_label='x_1', y_label='x_2')
        x1 = 4 + 3 * np.random.rand(30)
        x2 = np.random.choice([0, 1], 30)
        line1 = always_redraw(lambda: Line(start=axes.c2p(tracker1.get_value(), 0), end=axes.c2p(tracker1.get_value(), 1.2), color=BLUE))
        line2 = always_redraw(lambda: Line(start=axes.c2p(0, tracker2.get_value()), end=axes.c2p(10, tracker2.get_value()), color=RED))
        halfline1 = Line(start=axes.c2p(5.5, 0), end=axes.c2p(5.5, 0.5), color=BLUE)
        halfline2 = Line(start=axes.c2p(4.5, 0.5), end=axes.c2p(4.5, 1.2), color=BLUE)
        halfline3 = Line(start=axes.c2p(6, 0.5), end=axes.c2p(6, 1.2), color=GREEN)
        dots = [Dot((axes.c2p(i, j)), color=YELLOW) for i, j in zip(x1, x2)]
        text1 = Tex('Mean Of Region For Regression').shift(UP*1)
        text2 = Tex('Modal Class Of Region For Classification').shift(DOWN*1)

        self.play(LaggedStart(Create(axes), Create(axis_labels)), run_time=3)   
        self.play(LaggedStart(*[Write(dot) for dot in dots], lag_ratio=0.25, run_time=3))
        self.wait()
        self.play(Create(line1))
        self.wait()
        self.play(tracker1.animate.set_value(8), run_time=3)
        self.wait()
        self.play(tracker1.animate.set_value(1), run_time=3)
        self.wait()
        self.play(Uncreate(line1))
        self.play(Create(line2))
        self.wait()
        self.play(tracker2.animate.set_value(0.9), run_time=3)
        self.wait()
        self.play(tracker2.animate.set_value(0.1), run_time=3)
        self.wait()
        self.play(tracker2.animate.set_value(0.5))
        self.wait()
        self.play(Create(halfline1))
        self.wait()
        self.play(Create(halfline2))
        self.wait()
        self.play(Create(halfline3))
        self.wait()
        self.play(Uncreate(axes), Uncreate(axis_labels), Uncreate(line2), Uncreate(halfline1), Uncreate(halfline2), Uncreate(halfline3), *[Unwrite(dot) for dot in dots])
        self.play(LaggedStart(Write(text1), Write(text2), run_time=3, lag_ratio=0.75))
        self.wait()
        self.play(LaggedStart(Unwrite(text2), Unwrite(text1), run_time=3, lag_ratio=0.75))