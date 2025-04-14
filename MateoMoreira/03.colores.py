from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class myBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.label = Label(text="Hola Mundo")
        self.add_widget(self.label)
        btn = Button(text="Cambiar texto")
        btn.bind(on_press=self.change_text)
        self.add_widget(btn)

    def change_text(self, instance):
        self.label.text = "Has presionado el button"
    
class TestApp(App):
    def build(self):
        return myBoxLayout()
    
if __name__ == '__main__':
    TestApp().run()