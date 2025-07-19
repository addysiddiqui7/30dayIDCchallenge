'''This is the GUI version of old pass gen. but it dont have that while loop. I think that without GUI version was more cool'''

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.graphics import Rectangle
import string
import random

# Password generation functions
def password1(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def password2(length):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

def password3(length):
    return ''.join(random.choice(string.digits) for _ in range(length))

def password4(length):
    return ''.join(random.choice(string.hexdigits) for _ in range(length))


TEA_GREEN     = (213 / 255, 240 / 255, 192 / 255, 1)  # RGBA: (0.835, 0.941, 0.752, 1)
MINT_GREEN    = (152 / 255, 251 / 255, 152 / 255, 1)  # RGBA: (0.596, 0.984, 0.596, 1)
MAGIC_MINT    = (188 / 255, 235 / 255, 215 / 255, 1)  # RGBA: (0.737, 0.922, 0.843, 1)
SEAFOAM_GREEN = (158 / 255, 219 / 255, 197 / 255, 1)  # RGBA: (0.619, 0.859, 0.772, 1)
CELEDON       = (172 / 255, 225 / 255, 175 / 255, 1)  # RGBA: (0.674, 0.882, 0.686, 1)
PASTEL_GREEN  = (119 / 255, 221 / 255, 119 / 255, 1)  # RGBA: (0.467, 0.867, 0.467, 1)

class PasswordFloatApp(App):
    def build(self):
        layout = FloatLayout()

        # Set background image
        with layout.canvas.before:
            self.bg = Rectangle(source='bge3.jpg', pos=layout.pos, size=layout.size)
        layout.bind(pos=self._update_bg, size=self._update_bg)

        # Title Label
        title = Label(text="^_+ Password Generator by Addy Siddiqui",
                      font_size=24,
                      color=(1, 1, 0.9, 1),
                      bold=True,
                      size_hint=(.8, .1),
                      pos_hint={'center_x': .5, 'top': .95})
        layout.add_widget(title)

        # Password Length Input
        self.length_input = TextInput(hint_text='Password Length (8–16)',
                                      multiline=False,
                                      input_filter='int',
                                      size_hint=(.6, .06),
                                      pos_hint={'center_x': .5, 'top': .82},
                                      background_color=(1, 1, 1, 0.7),
                                      foreground_color=(0, 0, 0, 1))
        layout.add_widget(self.length_input)

        # Password Type Input
        self.type_input = TextInput(hint_text='Type: 1-Lower, 2-Both, 3-Digits, 4-Mixed',
                                    multiline=False,
                                    input_filter='int',
                                    size_hint=(.6, .06),
                                    pos_hint={'center_x': .5, 'top': .72},
                                    background_color=(1, 1, 1, 0.7),
                                    foreground_color=(0, 0, 0, 1))
        layout.add_widget(self.type_input)

        # Generate Button
        generate_btn = Button(text="Generate Password",
                              size_hint=(.4, .06),
                              pos_hint={'center_x': .5, 'top': .62},
                              background_color=(0, 0.6, 1, 1),
                              color=(1, 1, 1, 1))
        generate_btn.bind(on_press=self.generate_password)
        layout.add_widget(generate_btn)

        # Result Label
        self.result_label = Label(text="",
                                  font_size=18,
                                  color=(0.8, 1, 0.5, 1),
                                  size_hint=(.9, .15),
                                  pos_hint={'center_x': .5, 'top': .5})
        layout.add_widget(self.result_label)

        return layout

    def _update_bg(self, instance, value):
        self.bg.pos = instance.pos
        self.bg.size = instance.size

    def generate_password(self, instance):
        try:
            length = int(self.length_input.text)
            if not 8 <= length <= 16:
                self.result_label.text = "~_~! Length must be between 8 and 16."
                self.result_label.color= TEA_GREEN
                Label(
    
    markup=True
)

                return

            password_type = int(self.type_input.text)
            if password_type == 1:
                password = password1(length)
            elif password_type == 2:
                password = password2(length)
            elif password_type == 3:
                password = password3(length)
            elif password_type == 4:
                password = password4(length)
            else:
                self.result_label.text = "~_~! Type must be between 1 and 4."
                return

            self.result_label.text = f"^.^ Password Generated: {password}"
        except ValueError:
            self.result_label.text = "~_~! Enter valid numbers for length and type."


if __name__ == '__main__':
    PasswordFloatApp().run()
