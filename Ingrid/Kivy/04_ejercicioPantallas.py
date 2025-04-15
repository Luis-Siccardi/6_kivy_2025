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
            text: "ir a pantalla 2"
            pos_hint: {"center_x": 0.5, "center_y": 0.4}
            on_release: app.change_screen("pantalla2")
        
    MDScreen:
        name: "pantalla2"
        MDLabel:
            text: "Pantalla 2"
            halign: "center"
        MDFlatButton:
            text: "Volver a pantalla 1"
            pos_hint: {"center_x": 0.5, "center_y": 0.4}
            on_release: app.change_screen("pantalla1")
'''

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)
    
    def change_screen(self, screen_name):
        self.root.current = screen_name

MyApp().run()