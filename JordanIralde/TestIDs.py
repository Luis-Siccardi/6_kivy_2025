def validate_login(self):
        HomeScreen = self.root.get_screen("HomeScreen")
        username = HomeScreen.ids.text_input1.text.strip()
        password = HomeScreen.ids.text_input2.text.strip()

        if username and password:
            self.root.current = "SettingsScreen"
            self.mostrar_snackbar("✅ Login exitoso")
        else:
            self.mostrar_snackbar("⚠️ Completa todos los campos")
            
            
"""                Este es el contenido del archivo main.kv
                que se carga en la aplicación KivyMD.
                
    <HomeScreen@Screen>:
    name: "HomeScreen"
    BoxLayout:
        orientation: "vertical"
        spacing: dp(20)
        padding: dp(40)

        BoxLayout:
            size_hint_y: None
            height: dp(50)
            spacing: dp(10)
            Button:
                text: 'Ir a Settings'
                on_press: app.go_to_settings()

        MDTextField:
            id: text_input1


        MDTextField:
            id: text_input2
"""