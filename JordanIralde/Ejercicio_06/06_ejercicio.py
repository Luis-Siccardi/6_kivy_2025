from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDButton
from kivy.uix.screenmanager import ScreenManager, Screen

 
class MainApp(MDApp):
    dialog = None

    def build(self):
        return Builder.load_file("six.kv")

    def mostrar_dialogo(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Detalles del Usuario",
                text="Jordan, desarrollador y emprendedor. Email: jordan@ejemplo.com",
                buttons=[
                    MDButton(text="CERRAR", on_release=self.cerrar_dialogo),
                ],
            )
        self.dialog.open()

    def cerrar_dialogo(self, *args):
        self.dialog.dismiss()

MainApp().run()
