#!/usr/bin/env python

# To run: manimce -qh test.py

from manim import *

class Test(Scene):
    def construct(self):
        basel = MathTex(r"\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}")
        self.play(Write(basel))
        self.wait(3)