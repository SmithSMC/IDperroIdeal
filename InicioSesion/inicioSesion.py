from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout

class CasillaTexto(TextInput):
    pass

class EnlaceLabel(Label):
    pass

class EnlaceIniciaSesionLabel(Label):
    pass

class MainApp(App):
    def build(self):
        self.layout = RelativeLayout()

        Window.clearcolor = (1, 1, 1, 1)
        Window.size = (369, 640)

        background = Image(source='fondo4.png')
        self.layout.add_widget(background)

        welcome_label = Label(
            text="¡Bienvenido de nuevo!",
            color=(168/255, 110/255, 69/255, 1),
            size_hint=(None, None),
            size=(330, 60),
            pos_hint={'center_x': 0.5, 'center_y': 0.8},
            font_size='30sp',
            font_name='Inter.ttc',
            halign='center',
            valign='middle'
        )
        self.layout.add_widget(welcome_label)

        email_input = CasillaTexto(
            hint_text="Correo",
            multiline=False,
            background_color=(241/255, 194/255, 163/255, 1),
            foreground_color=(0, 0, 0, 1),
            border=(0, 0, 0, 0),
            background_active='',  # Eliminar sombreado al hacer clic
            size_hint=(None, None),
            size=(330, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.6},
            font_name='Inter.ttc'
        )
        password_input = CasillaTexto(
            hint_text="Contraseña",
            multiline=False,
            password=True,
            background_color=(241/255, 194/255, 163/255, 1),
            foreground_color=(0, 0, 0, 1),
            border=(0, 0, 0, 0),
            background_active='',  # Eliminar sombreado al hacer clic
            size_hint=(None, None),
            size=(330, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            font_name='Inter.ttc'
        )
        self.layout.add_widget(email_input)
        self.layout.add_widget(password_input)

        login_button = Button(
            text="Iniciar sesión",
            background_color=(168/255, 110/255, 69/255, 1),
            color=(1, 1, 1, 1),
            background_down='#A86E45',
            size_hint=(None, None),
            size=(330, 40),
            pos_hint={'center_x': 0.5, 'center_y': 0.4},
            font_name='Inter.ttc'
        )
        login_button.bind(on_press=self.verificar_contraseña)
        self.layout.add_widget(login_button)

        register_layout = BoxLayout(
            orientation='horizontal',
            size_hint=(None, None),
            size=(330, 40),
            pos_hint={'center_x': 0.55, 'center_y': 0.3}
        )

        register_label = Label(
            text="¿Eres nuevo? ",
            color=(0, 0, 0, 1),
            size_hint=(None, None),
            height=40,
            font_name='Inter.ttc'
        )
        register_layout.add_widget(register_label)

        register_button = Button(
            text="Regístrate aquí",
            background_normal='',
            background_color=(1, 1, 1, 0),
            color=(168/255, 110/255, 69/255, 1),
            size_hint=(None, None),
            height=40,
            pos_hint={'center_x': 0.55, 'center_y': 0.5},
            font_name='Inter.ttc',
            background_down='',
            bold=True
        )
        register_button.bind(on_press=self.ir_a_registro)
        register_layout.add_widget(register_button)

        self.layout.add_widget(register_layout)

        return self.layout

    def verificar_contraseña(self, instance):
        correo = self.layout.children[2].text  # Acceder al TextInput del correo
        contraseña = self.layout.children[3].text  # Acceder al TextInput de la contraseña

        # Lógica de verificación de la contraseña
        if contraseña == "contraseña_correcta":
            print("Contraseña correcta. Iniciando sesión...")
            # Aquí puedes agregar la lógica para iniciar sesión
        else:
            # Si la contraseña es incorrecta, mostrar un mensaje de error en color rojo
            error_label = Label(
                text="Contraseña incorrecta. Intentelo de nuevo",
                color=(1, 0, 0, 1),  # Rojo
                size_hint=(None, None),
                size=(330, 30),
                pos_hint={'center_x': 0.5, 'center_y': 0.3},
                font_name='Inter.ttc'
            )
            self.layout.add_widget(error_label)

    def ir_a_registro(self, instance):
        print("Ir a la pantalla de registro")

    def ir_a_inicio(self, instance):
        print("Ir a la pantalla de inicio")

if __name__ == '__main__':
    MainApp().run()
