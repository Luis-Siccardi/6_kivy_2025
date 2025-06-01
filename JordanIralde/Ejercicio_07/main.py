from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.snackbar.snackbar import (
    MDSnackbar,
    MD
)

from kivy.metrics import dp

class LoginApp(MDApp):
    def build(self):
        return Builder.load_file("main.kv")

    def go_to_settings(self):
        self.root.current = "SettingsScreen"

    def go_to_home(self):
        self.root.current = "HomeScreen"

    def validate_login(self):
        MDSnackbar(
            ,
            y=dp(24),
            pos_hint={"center_x": 0.5},
            size_hint_x=0.5,
        ).open()


LoginApp().run()
