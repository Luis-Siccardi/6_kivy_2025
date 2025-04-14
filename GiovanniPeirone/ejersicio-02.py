import os

os.environ['kivy_gl_backend'] = 'angle_sdl2' 

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class MainInterface(BoxLayout):
    def __init__(self, **kwargs):
        super(MainInterface, self).__init__(orientation='vertical', **kwargs)

        self.texto = Label(text = 'Hola Mundo', font_size=30)
        self.add_widget(self.texto)
        


class Main(App):
    def build(self):
        return MainInterface()

if __name__ == '__main__':
    Main().run()