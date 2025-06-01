from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar


class LoginApp(MDApp):
    def build(self):
        return Builder.load_file("main.kv")

    def go_to_settings(self):
        self.root.current = "SettingsScreen"

    def go_to_home(self):
        self.root.current = "HomeScreen"

    def validate_login(self):
        # Obtiene el texto ingresado en los campos, sin espacios extra al inicio/final
        user = self.root.ids.user_field.text.strip()
        pwd  = self.root.ids.pass_field.text.strip()

        # Verifica que ambos campos no estén vacíos
        if user and pwd:
            Snackbar(text="✅ Login exitoso").open()

        else:
            # Muestra un snackbar advirtiendo que complete los campos
            Snackbar(text="⚠️ Completa todos los campos").open()

LoginApp().run()
