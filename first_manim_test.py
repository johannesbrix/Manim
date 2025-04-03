# first manim program: 27.03.2025

from manim import *

class Pith(Scene):
    def construct(self):
        sq = Square(
            side_length=5, stroke_color=GREEN, fill_color=BLUE, fill_opacity = 0.75
        )
    
        self.play(Create(sq), run_time=3)
        self.wait()

class Testing(Scene):
    def construct(self):
        name = Tex("Johnanes").to_edge(UL, buff=0.5)
        sq = Square(side_length=0.5, fill_color=GREEN, fill_opacity=0.75).shift(LEFT * 3)
        tri = Triangle().scale(0.6).to_edge(DR)

        self.play(Write(name))
        self.play(DrawBorderThenFill(sq), run_time=2)
        self.play(Create(tri))
        self.wait()

        self.play(name.animate.to_edge(UR), run_time = 2)
        self.play(sq.animate.scale(2), tri.animate.to_edge(DL), run_time=3)
        self.wait()



class Getters(Scene):
    def construct(self):

        rect = Rectangle(color=WHITE, height=3, width=2.5).to_edge(UL)

        circ = Circle().to_edge(DOWN)

        # always redraw lambda makes the line follow the rectangle 
        arrow = always_redraw( lambda: Line(start=rect.get_bottom(), end=circ.get_top(), buff=0.5).add_tip())

        # the 3 objects get depicted
        self.play(Create(VGroup(rect, circ, arrow)))
        self.wait()
        # rectangle moves and circle scales at the same time
        self.play(rect.animate.to_edge(UR), circ.animate.scale(0.5), run_time=4)


# moving stuff together
class Updaters(Scene):
    def construct(self):

        num = MathTex("ln(2)")
        box = always_redraw(lambda : SurroundingRectangle(num, color=BLUE, fill_opacity=0.4, fill_color=RED, buff=0.5))
        name= always_redraw(lambda : Tex("Johannes").next_to(box, DOWN, buff=0.25))

        self.play(Create(VGroup(num, box, name)))
        self.play(num.animate.shift(RIGHT * 2), run_time=2)
        self.wait()


# make a counter or number updater
class ValueTrackers(Scene):
    def construct(self):

        k = ValueTracker(5)

        num = always_redraw(lambda : DecimalNumber().set_value(k.get_value()))

        self.play(FadeIn(num))
        self.wait()
        self.play(k.animate.set_value(0), run_time = 5, rate_func=smooth)


class Graphing(Scene):
    def construct(self):
        plane = NumberPlane(x_range=[-4, 4, 2], x_length=7, y_range=[0, 16, 2], y_length=5).to_edge(DOWN).add_coordinates()

        labels = plane.get_axis_labels(x_label="x", y_label="f(x)") 

        parab = plane.plot(lambda x: x**2, x_range=[-4, 4], color=GREEN)

        func_label = MathTex("f(x)=x^2").scale(0.6).next_to(parab, UR, buff=0.5).set_color(GREEN)

        area = plane.get_riemann_rectangles(graph = parab, x_range=[-2, 3], dx=0.1, stroke_color=WHITE)

        self.play(DrawBorderThenFill(plane))
        self.play(Create(VGroup(parab, labels)))
        self.wait()
        self.play(Create(area))
        self.wait()


class UpdaterGraphing(Scene):
    def construct(self):
        k = ValueTracker(-4)

        ax = Axes(x_range=[-4, 4, 1], 
                  y_range=[0, 16, 2], 
                  x_length=10, 
                  y_length=6
        ).add_coordinates()

        func = ax.plot(lambda x : x**2, x_range=[-4, 4], color=BLUE)

        slope = always_redraw(
            lambda : ax.get_secant_slope_group(
                x=k.get_value(), 
                graph=func, 
                dx=0.01, 
                secant_line_color=GREEN, 
                secant_line_length=3
            )
        )

        # c2p = coordinates to point
        pt = always_redraw(
            lambda : Dot().move_to(ax.c2p(k.get_value(), 
                                          k.get_value()**2))
        )   

        self.add(ax, func, slope, pt)
        self.wait()
        self.play(k.animate.set_value(4), run_time=3)
        self.wait()


Home = "Logo_vector_black_rectangle_without_bg.svg"

class SVGs(Scene):
    def construct(self):

        # pic has to be in the same or a follow-up folder
        icon = SVGMobject(file_name=f"{Home}").scale(0.5).to_edge(DR)

        image = ImageMobject("sally").scale(0.5).to_edge(DL)

        # only works with vectorized objects
        self.play(DrawBorderThenFill(icon))
        self.wait()
        self.play(FadeIn(image))
        






