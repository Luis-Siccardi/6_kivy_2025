#ejercicio 4

from kivy.config import Config
Config.set('graphics', 'withd', '393')
Config.set('graphics', 'height', '852')

from kivy.lang import Builder 
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivymd.app import MDApp

KV = '''
ScreenManager: 
    MenuScreen: 
    SettingsScreen: 

<MenuScreen>:
    name: 'menu' 
    MDLabel: 
        text:'Pantalla de inicio'
        halign:'center'
    MDRainsedButton: 
        text: 'Ir a Configuración'
        pos_hint:{'center_x': 0.5, 'center_y':0.4}
        on_release: 
            root.manager.current = 'settings'

<SettingsScreen>: 
    name:'settings' 
    MDLabel:
        text: 'Pantalla de configuación'
        halign: 'center'
    MDRaisedButton: 
        text: 'Volver al menu'
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        on_release: 
            root.manager.current = 'menu'
'''

class MenuScreen (Screen): 
    pass

class SettingScreen(Screen):
    pass

class MyApp(MDApp): 
    def build(self):
        return Builder.load_string(KV)
    
if __name__ == '__main__':
    MyApp().run()
