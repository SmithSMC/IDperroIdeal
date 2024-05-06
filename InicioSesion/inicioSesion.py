from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

Builder.load_string('''
<MainLayout>:
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            size: self.size
            pos: self.pos
            source: 'fondo4.png'

    Label:
        text: "¡Bienvenido de nuevo!"
        color: 168/255, 110/255, 69/255, 1
        size_hint: None, None
        size: 330, 60
        pos_hint: {'center_x': 0.5, 'center_y': 0.8}
        font_size: '30sp'
        font_name: 'Inter.ttc'
        halign: 'center'
        valign: 'middle'

    CasillaTexto:
        id: email_input
        hint_text: "Correo"
        multiline: False
        background_color: 241/255, 194/255, 163/255, 1
        foreground_color: 0, 0, 0, 1
        border: 0, 0, 0, 0
        background_active: ''
        size_hint: None, None
        size: 330, 40
        pos_hint: {'center_x': 0.5, 'center_y': 0.6}
        font_name: 'Inter.ttc'

    CasillaTexto:
        id: password_input
        hint_text: "Contraseña"
        multiline: False
        password: True
        background_color: 241/255, 194/255, 163/255, 1
        foreground_color: 0, 0, 0, 1
        border: 0, 0, 0, 0
        background_active: ''
        size_hint: None, None
        size: 330, 40
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        font_name: 'Inter.ttc'

    Button:
        text: "Iniciar sesión"
        background_color: 168/255, 110/255, 69/255, 1
        color: 1, 1, 1, 1
        background_down: '#A86E45'
        size_hint: None, None
        size: 330, 40
        pos_hint: {'center_x': 0.5, 'center_y': 0.4}
        font_name: 'Inter.ttc'
        on_press: root.verificar_contraseña()

    BoxLayout:
        orientation: 'horizontal'
        size_hint: None, None
        size: 330, 40
        pos_hint: {'center_x': 0.55, 'center_y': 0.3}

        Label:
            text: "¿Eres nuevo? "
            color: 0, 0, 0, 1
            size_hint: None, None
            height: 40
            font_name: 'Inter.ttc'

        Button:
            text: "Regístrate aquí"
            background_normal: ''
            background_color: 1, 1, 1, 0
            color: 168/255, 110/255, 69/255, 1
            size_hint: None, None
            height: 40
            pos_hint: {'center_x': 0.55, 'center_y': 0.5}
            font_name: 'Inter.ttc'
            background_down: ''
            bold: True
            on_press: root.ir_a_registro()
''')

class CasillaTexto(TextInput):
    pass

class MainLayout(RelativeLayout):
    def verificar_contraseña(self):
        correo = self.ids.email_input.text
        contraseña = self.ids.password_input.text

        if contraseña == "contraseña_correcta":
            print("Contraseña correcta. Iniciando sesión...")
            # Lógica para iniciar sesión
        else:
            # Mostrar mensaje de error
            print("Contraseña incorrecta. Intentelo de nuevo")

    def ir_a_registro(self):
        print("Ir a la pantalla de registro")

class MainApp(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)
        Window.size = (369, 640)
        return MainLayout()

if __name__ == '__main__':
    MainApp().run()
