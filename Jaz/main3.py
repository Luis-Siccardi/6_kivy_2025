from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation="vertical"
        self.label = Label(text="hola")
        self.add_widget(self.label)
        btn = Button (text="cambiar texto")
        btn.bind(on_press=self.change_text)
        self.add_widget(btn)
    
    def change_text(self, instance):
        self.label.text="presionaste el botón"

class TestApp(App):
    def build(self):
        return MyBoxLayout()
    
if __name__ == '__main__':
    TestApp().run()
    