from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image

class MainScreen(Screen):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        
        layout = FloatLayout()
        
        # Agregar imagen de fondo
        background = Image(source='fondo4.png', allow_stretch=True, keep_ratio=False)
        layout.add_widget(background)
        
        # Label de bienvenida centrado
        welcome_label = Label(text="¡Bienvenido de nuevo!", color=(168/255, 110/255, 69/255, 1), size_hint=(None, None), size=(330, 69), pos_hint={'center_x': 0.5, 'center_y': 0.8}, font_size='30sp', font_name='Roboto-Bold', halign='center', valign='middle')
        layout.add_widget(welcome_label)
        
        # Layout para inputs y botones
        input_layout = GridLayout(cols=1, size_hint=(None, None), size=(330, 200), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        
        # Inputs de correo y contraseña
        email_input = TextInput(hint_text="Correo", multiline=False, background_color=(241/255, 194/255, 163/255, 1), foreground_color=(0, 0, 0, 1), border=(1, 1, 1, 1), size_hint=(None, None), size=(330, 40))
        password_input = TextInput(hint_text="Contraseña", multiline=False, password=True, background_color=(241/255, 194/255, 163/255, 1), foreground_color=(0, 0, 0, 1), border=(1, 1, 1, 1), size_hint=(None, None), size=(330, 40))
        input_layout.add_widget(email_input)
        input_layout.add_widget(password_input)
        
        # Botón transparente para "¿Olvidó su contraseña?"
        forgot_password_button = Button(text="[color=(168/255, 110/255, 69/255, 1)]¿Olvidó su contraseña?[/color]", markup=True, background_normal='', background_color=(0, 0, 0, 0), size_hint_y=None, height=40)
        forgot_password_button.bind(on_press=self.forgot_password_click)
        input_layout.add_widget(forgot_password_button)
        
        # Botón de iniciar sesión
        login_button = Button(text="Iniciar sesión", background_color=(168/255, 110/255, 69/255, 1), color=(1, 1, 1, 1), background_down='#F1C2A3', size_hint=(None, None), size=(330, 40))
        input_layout.add_widget(login_button)
        
        # Texto de "¿Eres nuevo? Regístrate aquí"
        register_label = Label(text="[color=(168/255, 110/255, 69/255, 1)]¿Eres nuevo?[/color] [u][color=(168/255, 110/255, 69/255, 1)]Regístrate aquí[/color][/u]", markup=True, size_hint_y=None, height=40)
        input_layout.add_widget(register_label)
        
        layout.add_widget(input_layout)
        
        self.add_widget(layout)
    
    def forgot_password_click(self, instance):
        instance.text = "[color=0000FF]¿Olvidó su contraseña?[/color]"  # Cambiar el color del texto a azul al hacer clic

class MyApp(App):
    def build(self):
        sm = ScreenManager()
        main_screen = MainScreen(name='main')
        sm.add_widget(main_screen)
        return sm

    def on_start(self):
        Window.size = (369, 640)
        Window.clearcolor = (1, 1, 1, 1)  # Fondo blanco
        self.title = 'Ingreso'  # Cambiar el nombre de la ventana

if __name__ == '__main__':
    MyApp().run()
