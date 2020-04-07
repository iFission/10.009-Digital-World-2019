# 1 #
from kivy.app import App
from kivy.uix.label import Label


class AlternateApp(App):
    def build(self):
        self.label = Label(text='abc', font_size=72)  # creating widget
        self.label.bind(on_touch_down=self.alternative)
        self.state = 0  # declare state instance variable
        return self.label

    def alternative(self, instance, touch):
        if self.state == 0:
            self.label.text = 'ab'  # change widget created
            self.state = 1

        elif self.state == 1:
            self.label.text = 'abc'
            self.state = 0


if __name__ == '__main__':
    AlternateApp().run()