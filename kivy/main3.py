from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout



class myBoxLayout(BoxLayout):
    def __int__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation ="vertical"
        self.label=Label(text="hola mundo")
        self.add_widget(self.label)
        btn=Button(text="cambiar texto")
        self.add_widget(btn)

    def change_text(self, instace):
        self.label.text="has presionado el boton"
class TestApp(App):
        def build(self):
             return myBoxLayout

if __name__ == "__main__":
    TestApp().run()


    



    