from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label

# Crear una interfaz sencilla con un Label y un Button que, 
# al presionarlo, cambia el texto del label:
Builder.load_string("""
<PaginaUno>:
    BoxLayout:
        Button:
            text: 'cambiar texto'
            on_press: root.ids.labelCambiado.text = 'Texto cambiado'
        Label:
            id: labelCambiado
            text: 'Texto original'
            halign: 'center'
            valign: 'center'
    

""")

class PaginaUno(Screen):
    pass

class TestApp(App):
    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(PaginaUno(name='uno'))


        return sm

if __name__ == '__main__':
    TestApp().run()