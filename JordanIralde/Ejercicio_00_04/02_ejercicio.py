from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

Builder.load_string("""
<PaginaUno>:
    BoxLayout:
        Button:
            text: 'Pagina 1'
        Button:
            text: 'IR A PAGINA 2'
            on_press: root.manager.current = 'dos'

<PaginaDos>:
    BoxLayout:
        Button:
            text: 'Pagina 2'
        Button:
            text: 'IR A PAGINA 1'
            on_press: root.manager.current = 'uno'
""")

class PaginaUno(Screen):
    pass

class PaginaDos(Screen):
    pass

class TestApp(App):
    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(PaginaUno(name='uno'))
        sm.add_widget(PaginaDos(name='dos'))

        return sm

if __name__ == '__main__':
    TestApp().run()