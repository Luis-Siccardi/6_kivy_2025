from kivymd.app import MDApp
from kivy.uix.label import MDLavel
class myapp(MDApp):
    def build(self):
        return MDLavel(text="!hola mundo",haling="center")
if __name__ == "__main__":
    myapp().run()