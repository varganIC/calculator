from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivymd.app import MDApp

Window.size = (400, 500)


class Container(BoxLayout):
    operator = ""

    def change_7(self):
        self.text_input.text += self.but_7.text

    def change_8(self):
        self.text_input.text += self.but_8.text

    def change_9(self):
        self.text_input.text += self.but_8.text

    def change_4(self):
        self.text_input.text += self.but_4.text

    def change_5(self):
        self.text_input.text += self.but_5.text

    def change_6(self):
        self.text_input.text += self.but_6.text

    def change_1(self):
        self.text_input.text += self.but_1.text

    def change_2(self):
        self.text_input.text += self.but_2.text

    def change_3(self):
        self.text_input.text += self.but_3.text

    def change_0(self):
        if self.text_input.text == "0":
            self.text_input.text = self.but_0.text
        else:
            self.text_input.text += self.but_0.text

    def point(self):
        if self.text_input.text != "" and "." not in self.text_input.text:
            self.text_input.text += "."

    def clear(self):
        self.text_input.text = ""

    def proverka(self, str):
        try:
            if "." in str:
                str = float(str)
            else:
                str = int(str)
            return str
        except Exception:
            self.text_input.text = "Ошибка"

    def addition(self):
        self.part1 = self.proverka(self.text_input.text)
        self.text_input.text = ""
        self.operator = "+"

    def difference(self):
        self.part1 = self.proverka(self.text_input.text)
        self.text_input.text = ""
        self.operator = "-"

    def dividing(self):
        self.part1 = self.proverka(self.text_input.text)
        self.text_input.text = ""
        self.operator = "/"

    def multiplication(self):
        self.part1 = self.proverka(self.text_input.text)
        self.text_input.text = ""
        self.operator = "x"

    def calculation(self):
        part2 = self.proverka(self.text_input.text)
        try:
            if self.operator == "+":
                self.text_input.text = ""
                self.text_input.text = str(self.part1 + part2)
            elif self.operator == "-":
                self.text_input.text = ""
                self.text_input.text = str(self.part1 - part2)
            elif self.operator == "x":
                self.text_input.text = ""
                self.text_input.text = str(self.part1 * part2)
            elif self.operator == "/":
                try:
                    self.text_input.text = ""
                    self.text_input.text = str(self.part1 / part2)
                except ZeroDivisionError:
                    self.text_input.text = "Ошибка"
        except TypeError:
            self.text_input.text = "Ошибка"


class DuckyApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "Calculator"
        super().__init__(**kwargs)

    def build(self):
        return Container()


if __name__ == "__main__":
    DuckyApp().run()