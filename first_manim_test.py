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

