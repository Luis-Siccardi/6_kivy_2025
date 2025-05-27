# main.py

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar

class LoginApp(MDApp):
    def build(self):
        # Carga el archivo KV que contiene toda la interfaz
        return Builder.load_file("main.kv")
    def go_to_settings(self):
        # Cambia a la pantalla de configuración
        cambiar = self.root.ids.screen_manager.current = "SettingsScreeen"

    def validate_login(self):
        # Obtiene el texto ingresado en los campos, sin espacios extra al inicio/final
        print("Validando login...")
        user = self.root.ids.user_field.text.strip()
        pwd  = self.root.ids.pass_field.text.strip()

        # Verifica que ambos campos no estén vacíos
        if user and pwd:
            # Muestra un snackbar con éxito
            Snackbar(text="✅ Login exitoso").open()

        else:
            # Muestra un snackbar advirtiendo que complete los campos
            Snackbar(text="⚠️ Completa todos los campos").open()


if __name__ == "__main__":
    # Punto de entrada de la aplicación
    LoginApp().run()