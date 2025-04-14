import os
from kivy.app import App
from kivy.uix.label import Label

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'  # Windows


class MyApp(App):
    def build(self):
        app = self
        return Label(text='¡Hola Mundo!')
    
if __name__ == '__main__':
    MyApp().run()