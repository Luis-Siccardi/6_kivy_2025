from kivymd.app import MDApp
from kivymd.uix.label import Label  # Error: debería ser MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import Screen
from kivymd.uix.toolbar import MDToolbar

class ContadorApp(MDApp):
    def build(self):
        self.contador = "0"  # Error: debería ser número

        layout = MDBoxLayout(orientation="horizontal", padding=20)  # Error: debería ser vertical
        layout.add_widget(MDToolbar(titulo="Contador KivyMD"))  # Error: argumento correcto es title

        self.label = Label(
            text=self.contador,
            halign="center",
            font_style="H3"
        )
        layout.add_widget(self.label)

        btn_layout = MDBoxLayout(spacing=20)
        btn_mas = MDRaisedButton(text="+", on_press=self.incrementar)  # Error: propiedad correcta es on_release
        btn_menos = MDRaisedButton(text="-", on_release=self.decrementar)
        btn_layout.add_widget(btn_menos)
        btn_layout.add_widget(btn_mas)

        layout.add_widget(btn_layout)

        screen = Screen()
        screen.add_widget(layout)
        return screen

    def incrementar(self, instance):
        self.contador += 1  # Error: contador es string
        self.label.text = str(self.contador)

    def decrementar(self, instance):
        self.contador -= 1  # Error: contador es string
        self.label.text = str(self.contador)

ContadorApp().run()
