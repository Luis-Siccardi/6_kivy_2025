from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class PrimeraPantalla(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        boton = Button(text="Ir a la Segunda Pantalla")
        boton.bind(on_press=self.cambiar_pantalla)
        layout.add_widget(boton)
        self.add_widget(layout)

    def cambiar_pantalla(self, instance):
        self.manager.current = "segunda"

class SegundaPantalla(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical')
        boton = Button(text="Volver a la Primera Pantalla")
        boton.bind(on_press=self.cambiar_pantalla)
        layout.add_widget(boton)
        self.add_widget(layout)

    def cambiar_pantalla(self, instance):
        self.manager.current = "primera"

class MiApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(PrimeraPantalla(name="primera"))
        sm.add_widget(SegundaPantalla(name="segunda"))
        return sm

MiApp().run()
