from kivy.lang import Builder
from kivymd.app import MDApp

KV = '''
ScreenManager:
MDScreen:
    name: 'uno'
    id : screen_manager
    MDLabel:
        text: 'Pagina 1'
        halign: 'center'
    MDFlatButton:
        text: 'IR A PAGINA 2'
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.change_screen('dos')
    MDFlatButton:
        text: 'IR A PAGINA 3'
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.change_screen('tres')
    PaginaDos:
        name: 'dos'
    PaginaTres:
        name: 'tres'
        

'''

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)
    
    def change_screen(self, screen_name):
        self.root.current = screen_name
        
MyApp().run()