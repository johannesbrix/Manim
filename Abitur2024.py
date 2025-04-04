from manim import *

class Scene1(Scene):
    def construct(self):
        # write the task
        geg = Tex(r"Gegeben ist die in $\mathbb{R}$ definierte Funktion $f: x \mapsto 8x^2 + 3x$ mit der Ableitungsfunktion $f'$.").scale(0.5).move_to(UP)
        num = Text("Teilaufgabe Teil A 1a", weight=BOLD).scale(0.7)
        aufgabe = Tex(r"Berechnen Sie $f'(1)$.").move_to(DOWN)
        
        # write what they search for
        self.play(Create(geg))
        self.wait()
        self.play(FadeIn(num))
        self.wait()
        self.play(FadeIn(aufgabe))
        self.wait()

        aufgabenstellung = VGroup(geg, num, aufgabe)

        self.play(aufgabenstellung.animate.scale(0.5).move_to(LEFT * 5 + UP * 2.5))
        self.wait()


class Scene2(Scene):
    def construct(self):
        tex = Tex("Wir bilden die Ableitung:").move_to(4*LEFT + 3 * UP).scale(0.5)
        formula1 = MathTex(r"f(x) = 8x^3+3x=").move_to(4*LEFT + 2 * UP).scale(0.5)
        formula2 = MathTex(r"f'(x) = 24x^2 + 3").move_to(4*LEFT + 1 * UP).scale(0.5)
        formula3 = MathTex(r"f'(1) = 24 \cdot 1^2 + 3 = 27").move_to(4*LEFT).scale(0.5)

        self.play(Create(tex))
        self.wait()
        self.play(Create(formula1))
        self.wait()
        self.play(Transform(formula1, formula2))
        self.wait()
        self.play(Create(formula3))
        self.wait()


class Scene3(Scene):
    def construct(self):
        area = Axes(x_range=(-2, 2, 1), 
                    x_length=8, y_range=(-80, 80, 40),
        ).to_edge(DOWN).add_coordinates()

        labels = area.get_axis_labels(x_label="x", y_label="f(x)")

        self.add(area)
        self.wait()

        f_x = area.plot(lambda x: 8*x**3 + 3*x, x_range=[-2, 2], color=BLUE)

        self.play(Create(f_x))
        self.wait()

        F_x = area.plot(lambda x: 2 * x ** 4 + 3 / 2 * x ** 2, x_range=[-2, 2], color=RED)

        self.play(Create(F_x))
        self.wait()

        k = ValueTracker(-2)

        pt1 = always_redraw(
            lambda : Dot().move_to(area.c2p(k.get_value(), 
                                          8*k.get_value()**3 + 3*k.get_value()))
        ) 

        pt2 = always_redraw(
            lambda : Dot().move_to(area.c2p(k.get_value(), 
                                          2*k.get_value()**4 + (3/2)*k.get_value()**2))
        ) 

        self.add(pt1, pt2)
        self.wait()

        h1_line = always_redraw(
            lambda: Line(
                start=area.c2p(area.x_range[0], 8*k.get_value()**3 + 3*k.get_value()),
                end=pt1.get_center(),
                color=YELLOW
            )
        )

        h2_line = always_redraw(
            lambda: Line(
                start=area.c2p(area.x_range[0], 2*k.get_value()**4 + (3/2)*k.get_value()**2),
                end=pt2.get_center(),
                color=RED
            )
        )

        self.play(
            Create(h1_line),
            Create(h2_line)
        )

        self.wait()

        self.play(k.animate.set_value(2), run_time=3)
        self.wait()

        self.play(FadeOut(VGroup(area, pt1, pt2, h1_line, h2_line)))
