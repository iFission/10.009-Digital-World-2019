from kivy.app import App
from kivy.uix.label import Label


class MyLabel(Label):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_size = 69


class SlideDetectApp(App):
    def build(self):
        self.label = MyLabel(text='Slide Me')
        self.label.bind(on_touch_move=self.detect)
        return self.label

    def detect(self, instance, touch):
        if touch.dx < -10:
            instance.text = 'Slide Left'
        elif touch.dx > 10:
            instance.text = 'Slide Right'
        elif touch.dy < -10:
            instance.text = 'Slide Down'
        elif touch.dy > 10:
            instance.text = 'Slide Up'


if __name__ == '__main__':
    SlideDetectApp().run()