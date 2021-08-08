from manim import *


class InterningExample1(Scene):
    def construct(self):
        self.camera.background_color = DARK_BLUE
        code = '''>>> a = -5
>>> b = -5
>>> a is b
True    
        '''
        code1 = Code(
            code=code, tab_width=4, background="window",
            language="Python", font="Monospace", style='fruity'
        )
        code1_copy = code1.copy().shift(UP * 2, LEFT * 4)
        self.play(
            Transform(code1, code1_copy)
        )
        self.wait(3)
        code2 = '''>>> a = 256
>>> b = 256
>>> a is b
True    
        '''
        code2 = Code(
            code=code2, tab_width=4, background="window",
            language="Python", font="Monospace", style='fruity'
        )
        code2_copy = code2.copy().shift(UP * 2, RIGHT * 4)
        self.play(
            Transform(code2, code2_copy)
        )
        self.wait(3)

        code3 = '''>>> a = -6
>>> b = -6
>>> a is b
False    
        '''
        code3 = Code(
            code=code3, tab_width=4, background="window",
            language="Python", font="Monospace", style='fruity'
        )
        code3_copy = code3.copy().shift(DOWN * 2, LEFT * 4)
        self.play(
            Transform(code3, code3_copy)
        )
        self.wait(3)
        code4 = '''>>> a = 257
>>> b = 257
>>> a is b
False    
        '''
        code4 = Code(
            code=code4, tab_width=4, background="window",
            language="Python", font="Monospace", style='fruity'
        )
        code4_copy = code4.copy().shift(DOWN * 2, RIGHT * 4)
        self.play(
            Transform(code4, code4_copy)
        )
        self.wait(3)


class InterningNumberLine(Scene):
    def construct(self):
        self.camera.background_color = DARK_BLUE
        l0 = NumberLine(
                x_range=[-60, 290, 20],
                length=10,
                color=RED,
                include_numbers=True,
                label_direction=UP,
                numbers_to_include=[-5, 256]
            )
        [neg5] = [num for num in l0.numbers if num.number == -5]
        print([neg5], neg5)
        neg5.set_color(YELLOW)
        [p256] = [num for num in l0.numbers if num.number == 256]
        p256.set_color(YELLOW)
        self.play(Write(l0), run_time=3)
        self.wait(2)

class WhatIs(Scene):
    def construct(self):
        self.camera.background_color = DARK_BLUE
        condition1 = MathTex(r"-5 \geq a \leq +256 \\ -5 \geq b \leq +256"
        )
        condition_target1 = condition1.copy().shift(LEFT * 5)
        self.play(
            Transform(condition1, condition_target1),
            run_time=2
        )
        memory_locs = Table(
            [
                [":"],
                [":"],
                ["0x...FE"],
                ["0x...FF"],
                ["0x...00"],
                ["0x...01"],
                ["0x...02"],
                ["0x...03"],
                ["0x...04"],
                ["0x...05"],
                [":"],
                [":"],
            ],
            include_outer_lines=True,
        ).scale(0.5)
        mem_loc_right = memory_locs.copy().shift(RIGHT*2)
        self.play(Write(memory_locs), run_time=2)
        self.play(
            Transform(memory_locs, mem_loc_right)
        )
        self.wait(2)

        s = Square(side_length=1)
        a = Text("a")
        sa = VGroup(s, a)
        self.play(
            sa.animate.shift(UP * 2, LEFT * 2)
        )
        self.wait(2)

        s_copy = Square(side_length=1)
        b = Text("b")
        sb = VGroup(s_copy, b)
        self.play(
            sb.animate.shift(DOWN * 2, LEFT * 2)
        )
        self.wait(2)

        arrow_1 = Arrow(start=[-1.5, 1.5, 0], end=[1.1, -0.2, 0], stroke_width=3).scale(1.2)
        self.play(
            Write(arrow_1)
        )
        self.wait(2)
        
        arrow_2 = Arrow(start=[-1.5, -1.5, 0], end=[1.1, -0.2, 0], stroke_width=3).scale(1.2)
        self.play(
            Write(arrow_2)
        )
        self.wait(2)

class WhatIs2(Scene):
    def construct(self):
        self.camera.background_color = DARK_BLUE
        condition1 = MathTex(r"-5 \le a \ge +256 \\ -5 \le b \ge +256"
        )
        condition_target1 = condition1.copy().shift(LEFT * 5)
        self.play(
            Transform(condition1, condition_target1),
            run_time=2
        )
        memory_locs = Table(
            [
                [":"],
                [":"],
                ["0x...FE"],
                ["0x...FF"],
                ["0x...00"],
                ["0x...01"],
                ["0x...02"],
                ["0x...03"],
                ["0x...04"],
                ["0x...05"],
                [":"],
                [":"],
            ],
            include_outer_lines=True,
        ).scale(0.5)
        mem_loc_right = memory_locs.copy().shift(RIGHT*2)
        self.play(Write(memory_locs), run_time=2)
        self.play(
            Transform(memory_locs, mem_loc_right)
        )
        self.wait(2)

        s = Square(side_length=1)
        a = Text("a")
        sa = VGroup(s, a)
        self.play(
            sa.animate.shift(UP * 2, LEFT * 2)
        )
        self.wait(2)

        s_copy = Square(side_length=1)
        b = Text("b")
        sb = VGroup(s_copy, b)
        self.play(
            sb.animate.shift(DOWN * 2, LEFT * 2)
        )
        self.wait(2)

        arrow_1 = Arrow(start=[-1.5, 1.5, 0], end=[1.1, 0.8, 0], stroke_width=3).scale(1.2)
        self.play(
            Write(arrow_1)
        )
        self.wait(2)
        
        arrow_2 = Arrow(start=[-1.5, -1.5, 0], end=[1.1, -0.8, 0], stroke_width=3).scale(1.2)
        self.play(
            Write(arrow_2)
        )
        self.wait(2)


class InterningDef(Scene):
    def construct(self):
        self.camera.background_color = DARK_BLUE
        tit = MarkupText("ഇന്റേണിങ്", font="gayathri").scale(1)
        tit.shift(UP * 3)
        t = MarkupText("""
                ഇന്റേണിങ് എന്ന് പറയുന്നത്, ഇമ്മ്യൂട്ടബിൾ ആയ 
                ഒബ്ജക്റ്റിൻ്റെ ഒരു കോപ്പി മാത്രമേ മെമ്മറി ലൊക്കേഷനിൽ 
                രൂപപ്പെടുന്നുള്ളൂ എന്ന് ഉറപ്പാക്കാൻ ഉള്ള ഒരു ഉപാധിയാണ്.
            """, font='gayathri', justify=True, 
        ).scale(0.7)
        t.shift(UP)
        g = VGroup(tit, t)
        self.play(Write(g), run_time=5)
        self.wait(2)

class StringInterningExample(Scene):
    def construct(self):
        self.camera.background_color = DARK_BLUE
        code = '''>>> a = "helloworld"
>>> b = "helloworld"
>>> a is b
True'''
        code1 = Code(
            code=code, tab_width=4, background="window",
            language="Python", font="Monospace", style='fruity'
        )
        code1_copy = code1.copy().shift(UP * 2, LEFT * 4)
        self.play(
            Transform(code1, code1_copy)
        )
        self.wait(3)
        code2 = '''>>> a = "hello world"
>>> b = "hello world"
>>> a is b
False'''
        code2 = Code(
            code=code2, tab_width=4, background="window",
            language="Python", font="Monospace", style='fruity'
        )
        code2_copy = code2.copy().shift(UP * 2, RIGHT * 4)
        self.play(
            Transform(code2, code2_copy)
        )
        self.wait(3)

        code3 = '''>>> a = "helloworld!"
>>> b = "helloworld!"
>>> a is b
False'''
        code3 = Code(
            code=code3, tab_width=4, background="window",
            language="Python", font="Monospace", style='fruity'
        )
        code3_copy = code3.copy().shift(DOWN * 2)
        self.play(
                Transform(code3, code3_copy)
            )
        self.wait(3)
       