from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class Pantalla1(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        label = Label(text="Pantalla 1")
        boton = Button(text="Ir a Pantalla 2", on_press=self.cambiar_pantalla)

        layout.add_widget(label)
        layout.add_widget(boton)
        self.add_widget(layout)

    def cambiar_pantalla(self, instance):
        self.manager.current = "pantalla2"

class Pantalla2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')

        label = Label(text="Pantalla 2")
        boton = Button(text="Ir a Pantalla 1", on_press=self.cambiar_pantalla)

        layout.add_widget(label)
        layout.add_widget(boton)
        self.add_widget(layout)

    def cambiar_pantalla(self, instance):
        self.manager.current = "pantalla1"

class MiAplicacion(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(Pantalla1(name="pantalla1"))
        sm.add_widget(Pantalla2(name="pantalla2"))
        return sm

MiAplicacion().run()
