from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MiAplicacion(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.label = Label(text="Texto original")
        boton = Button(text="Presionar", on_press=self.cambiar_texto)

        layout.add_widget(self.label)
        layout.add_widget(boton)

        return layout

    def cambiar_texto(self, instance):
        self.label.text = "¡Texto cambiado!"

MiAplicacion().run()
