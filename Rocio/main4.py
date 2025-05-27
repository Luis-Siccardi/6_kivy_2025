from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


# crear una aplicación con dos pantallas.
# Con un botón se cambia de la primera pantalla
# a la segunda y viceversa:

from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
ScreenManager:
    id: screen_manager

    MDScreen:
        name: "pantalla1"
        MDLabel:
            text: "Pantalla 1"
            halign: "center"
        MDFlatButton:
            text: "Ir a Pantalla 2"
            pos_hint: {"center_x": 0.5, "center_y": 0.4}
            on_release: app.change_screen("pantalla2")
        MDFlatButton:
            text: "Ir a Pantalla 3"
            pos_hint: {"center_x": 0.5, "center_y": 0.3}
            on_release: app.change_screen("pantalla3")

    MDScreen:
        name: "pantalla2"
        MDLabel:
            text: "Pantalla 2"
            halign: "center"
        MDFlatButton:
            text: "Volver a Pantalla 1"
            pos_hint: {"center_x": 0.5, "center_y": 0.4}
            on_release: app.change_screen("pantalla1")

    MDScreen:
        name: "pantalla3"
        MDLabel:
            text: "Pantalla 3"
            halign: "center"
        MDFlatButton:
            text: "Volver a Pantalla 1"
            pos_hint: {"center_x": 0.5, "center_y": 0.4}
            on_release: app.change_screen("pantalla1")
'''

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def change_screen(self, screen_name):
        self.root.current = screen_name

MyApp().run()
