from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MyBoxLayout(BoxLayout):
    def __init__(self, **kwargs): 
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.label =Label(text="¡hola mundo!")
        self.add_widget(self.label)
        btn=Button(text="Cambiar text")
        btn.bind(on_press=self.change_text)
        self.add_widget(btn)

    def change_text(self, instance):
        self.label.text="¡HAS PRECIONADO EL BOTON!"
    
class  TestApp(App):
    def build(self):
        return MyBoxLayout()
    
if __name__=='__main__':
    TestApp().run()