from kivymd.app import MDApp
from kivymd.uix.snackbar import MDSnackbar
from kivymd.uix.button import MDButton
from kivymd.uix.label import MDLabel
from kivy.lang import Builder

KV = '''
MDScreen:
    MDButton:
        text: "Mostrar Snackbar"
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        on_release: app.mostrar_snackbar()
'''

class TestApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def mostrar_snackbar(self):
        snackbar = MDSnackbar(
            MDLabel(
            text="¡Hola! Este es un Snackbar personalizado.",
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1),
            halign="center",
            valign="middle",
        ),
            duration=5,
            orientation='vertical',
            background_color=(0.1, 0.6, 0.9, 1),
        )
        snackbar.open()


if __name__ == "__main__":
    TestApp().run()
