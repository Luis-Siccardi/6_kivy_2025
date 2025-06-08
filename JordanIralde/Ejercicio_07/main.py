from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.snackbar.snackbar import (
    MDSnackbar,
)

from kivy.metrics import dp


class LoginApp(MDApp):
    def build(self):
        return Builder.load_file("main.kv")
    
    def go_to_settings(self):
        self.root.current = "SettingsScreen"

    def go_to_home(self):
        self.root.current = "HomeScreen"

    def mostrar_snackbar(self, mensaje):
        snackbar = MDSnackbar(
            MDLabel(
            text=mensaje,
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            halign="center",
            valign="middle",
        ),
            duration=2,
            orientation='vertical',
            background_color=(0.1, 0.6, 0.9, 1),
        )
        return snackbar.open()
    
    def validate_login(self):
        HomeScreen = self.root.get_screen("HomeScreen")
        username = HomeScreen.ids.text_input1.text.strip()
        password = HomeScreen.ids.text_input2.text.strip()

        if username and password:
            self.root.current = "SettingsScreen"
            self.mostrar_snackbar("✅ Login exitoso")
        else:
            self.mostrar_snackbar("⚠️ Completa todos los campos")


if __name__ == "__main__":
    LoginApp().run()
