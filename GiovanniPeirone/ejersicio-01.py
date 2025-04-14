import os

os.environ['kivy_gl_backend'] = 'angle_sdl2'  # windows

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MiInterfaz(BoxLayout):
    def __init__(self, **kwargs):
        super(MiInterfaz, self).__init__(orientation='vertical', **kwargs)

        # Crear un Label
        self.mi_label = Label(text='Texto original', font_size=24)
        self.add_widget(self.mi_label)

        # Crear un Button
        boton = Button(text='Cambiar texto', size_hint=(1, 0.3))
        boton.bind(on_press=self.cambiar_texto)
        self.add_widget(boton)

    def cambiar_texto(self, instance):
        self.mi_label.text = '¡Texto cambiado!'

class MiApp(App):
    def build(self):
        return MiInterfaz()

if __name__ == '__main__':
    MiApp().run()