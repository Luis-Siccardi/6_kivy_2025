from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MiApp(App):
    def build(self):
        caja = BoxLayout(orientation='vertical')
        
        self.label = Label(text="Hola Mundo")
        boton = Button(text="Cambiar texto")
        
        boton.bind(on_press=self.cambiar_texto)
        
        caja.add_widget(self.label)
        caja.add_widget(boton)
        
        return caja

    def cambiar_texto(self, instance):
        self.label.text = "Chau Mundo"

MiApp().run()
