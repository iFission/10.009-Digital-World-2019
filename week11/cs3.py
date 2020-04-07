from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import kivy.input
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput


class InvestmentValueCalculator(App):
    def build(self):
        layout = GridLayout(cols=2)

        LabelPrompt1 = Label(text='Investment Amount', font_size=24)
        LabelPrompt2 = Label(text='Years', font_size=24)
        LabelPrompt3 = Label(text='Annual Interest Rate', font_size=24)
        LabelPrompt4 = Label(text='Future Value', font_size=24)
        self.TxtInput1 = TextInput(
            text='10000', font_size=24, input_filter='float', multiline=False
        )  # make it an instance vairable so can access it anywhere in the class
        self.TxtInput2 = TextInput(text='3',
                                   font_size=24,
                                   input_filter='float')
        self.TxtInput3 = TextInput(text='3.25',
                                   font_size=24,
                                   input_filter='float')
        MyButton = Button(text='Calculate', font_size=24)
        MyButton.bind(on_press=self.change)
        self.LabelResult = Label(text='Result', font_size=24)

        # sequence of layout is important
        layout.add_widget(LabelPrompt1)
        layout.add_widget(self.TxtInput1)
        layout.add_widget(LabelPrompt2)
        layout.add_widget(self.TxtInput2)
        layout.add_widget(LabelPrompt3)
        layout.add_widget(self.TxtInput3)
        layout.add_widget(LabelPrompt4)
        layout.add_widget(self.LabelResult)
        layout.add_widget(MyButton)

        return layout

    def change(self, instance):
        Amount = float(self.TxtInput1.text)
        Years = float(self.TxtInput2.text)
        ir = float(self.TxtInput3.text)
        fv = Amount * ((1 + (ir / 1200))**(Years * 12))
        self.LabelResult.text = str(fv)


if __name__ == '__main__':
    # instantiate the class above
    InvestmentValueCalculator().run()