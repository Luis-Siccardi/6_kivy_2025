'''
# Ejercicio 5: Interfaz de Inicio de Sesión con KivyMD

**Objetivo:**  
Crear una interfaz de usuario de inicio de sesión utilizando los componentes de KivyMD, 
manteniendo la estética del Material Design.

**Enunciado:**  
Desarrolla una aplicación en KivyMD que presente un formulario de inicio de sesión con los 
siguientes elementos:

- **MDToolbar:**  
  - Ubicada en la parte superior, con el título `"Inicio de Sesión"`.

- **MDTextField:**  
  - Dos campos de texto:
    - Uno para el usuario.
    - Uno para la contraseña, con la propiedad `password: True` para ocultar los caracteres.

- **MDFlatButton o MDRaisedButton:**  
  - Un botón con la etiqueta `"Ingresar"`.

- **Validación sencilla:**  
  - Cuando se presione el botón `"Ingresar"`, se debe verificar que ambos campos (usuario y contraseña) tengan contenido.
  - Si ambos campos están completos, muestra un **MDDialog** con el mensaje de bienvenida, por ejemplo:  
    `"Bienvenido, [Usuario]!"`
  - Si alguno de los campos está vacío, muestra un **MDDialog** con un mensaje de error, como:  
    `"Por favor, complete ambos campos."`

**Extras (Opcionales):**  
- Personaliza la paleta de colores y el tema (claro u oscuro) usando las propiedades de `theme_cls` para mantener la coherencia con el Material Design.
- Agrega algún icono representativo (por ejemplo, en la MDToolbar o en alguno de los botones) utilizando la librería de Material Icons integrada en KivyMD.

'''

from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.m

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