from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager


#
class MenuScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layout = BoxLayout()
        #
        button_settings = Button(text='Settings', font_size=48)
        button_quit = Button(text='Quit', font_size=48)
        #
        button_settings.bind(on_press=self.change_to_setting)
        button_quit.bind(on_press=self.quit_app)
        #
        self.layout.add_widget(button_settings)
        self.layout.add_widget(button_quit)
        #
        self.add_widget(self.layout)  # screen is a layout itself
#

    def change_to_setting(self, value):
        self.manager.transition.direction = 'left'
        # modify the current screen to a different "name"
        self.manager.current = 'settings'

    def quit_app(self, value):
        App.get_running_app().stop()


#
class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        self.layout = BoxLayout()
        # Add your code below to add the label and the button
        label_setting_screen = Label(text='Settings Screen', font_size=48)
        button_menu = Button(text='Back to Menu', font_size=48)
        #
        button_menu.bind(on_press=self.change_to_menu)
        #
        self.layout.add_widget(label_setting_screen)
        self.layout.add_widget(button_menu)
        #
        self.add_widget(self.layout)

    def change_to_menu(self, value):
        self.manager.transition.direction = 'right'
        # modify the current screen to a different "name"
        self.manager.current = 'menu'


class SwitchScreenApp(App):
    def build(self):
        sm = ScreenManager()
        ms = MenuScreen(name='menu')
        st = SettingsScreen(name='settings')
        sm.add_widget(ms)
        sm.add_widget(st)
        sm.current = 'menu'
        return sm


if __name__ == '__main__':
    SwitchScreenApp().run()
