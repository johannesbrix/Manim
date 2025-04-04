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
        self.play(Create(num))
        self.wait()
        self.play(Create(aufgabe))
        self.wait()

        aufgabenstellung = VGroup(geg, num, aufgabe)

        self.play(aufgabenstellung.animate.scale(0.5).move_to(LEFT * 5 + UP * 2.5))
        self.wait()


