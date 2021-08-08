from manim import *

class Intro(Scene):
  def construct(self):
    self.camera.background_color = DARK_BLUE
    logo_green = "#87c2a5"
    # logo_black = "#343434"
    logo_blue = "#525893"
    logo_red = "#e07a5f"
    circle = Circle(0.9, color=logo_blue, fill_opacity=1).shift(LEFT * 2.7)
    self.wait(0.5)
    my = MathTex(r"\mathbb{\text{My}}", fill_color=logo_red).scale(2)
    my.shift(LEFT * 2.6)
    self.wait(0.3)
    stackquest = MathTex(r"\mathbb{\text{ StackQuest}}", fill_color=logo_green).scale(2)
    stackquest.shift(RIGHT, 0.1 * LEFT)
    logo = VGroup(circle, my, stackquest)
    self.play(Write(logo), run_time=2.5)
    self.wait()