from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import Rectangle

class TempApp(App):
    def build(self):
        layout = FloatLayout()

        # Set background image using canvas
        with layout.canvas.before:
            self.bg = Rectangle(source='bg3.jpeg', pos=layout.pos, size=layout.size)
        layout.bind(size=self._update_bg, pos=self._update_bg)

        # Title Label
        title = Label(text="Temperature Converter by Addy Siddiqui",
                      font_size=24,
                      color = (0.95, 0.95, 1, 1),
                      bold=True,
                      size_hint=(.8, .1),
                      pos_hint={'center_x': .5, 'top': .95})
        layout.add_widget(title)

        # Temperature Input
        self.temp_input = TextInput(hint_text='Temperature',
                                    multiline=False,
                                    size_hint=(.6, .06),
                                    pos_hint={'center_x': .5, 'top': .8},
                                    background_color=(1, 1, 1, 0.7),
                                    foreground_color=(0, 0, 0, 1),
                                    padding_y=(10, 10))
        layout.add_widget(self.temp_input)

        # Unit Input
        self.unit_input = TextInput(hint_text='Unit (C/F/K)',
                                    multiline=False,
                                    size_hint=(.6, .06),
                                    pos_hint={'center_x': .5, 'top': .72},
                                    background_color=(1, 1, 1, 0.7),
                                    foreground_color=(0, 0, 0, 1),
                                    padding_y=(10, 10))
        layout.add_widget(self.unit_input)

        # Convert Button
        convert_btn = Button(text="Convert",
                             size_hint=(.4, .06),
                             pos_hint={'center_x': .5, 'top': .63},
                             background_color=(1, 0.5, 0, 1),  # orange
                             color=(1, 1, 1, 1))
        convert_btn.bind(on_press=self.convert_temp)
        layout.add_widget(convert_btn)

        # Result Label
        self.result_label = Label(text="",
                                  font_size=18,
                                  color=(0.2, 1, 0.6, 1),  # highlighted teal
                                  size_hint=(.9, .15),
                                  pos_hint={'center_x': .5, 'top': .5})
        layout.add_widget(self.result_label)

        return layout

    def _update_bg(self, instance, value):
        self.bg.pos = instance.pos
        self.bg.size = instance.size

    def convert_temp(self, instance):
        try:
            temp = float(self.temp_input.text)
            unit = self.unit_input.text.lower()

            if unit == 'c':
                f = (temp * 9/5) + 32
                k = temp + 273.15
                result = f"Fahrenheit: {round(f, 2)}°F\nKelvin: {round(k, 2)}K"
            elif unit == 'f':
                c = (temp - 32) * 5/9
                k = c + 273.15
                result = f"Celsius: {round(c, 2)}°C\nKelvin: {round(k, 2)}K"
            elif unit == 'k':
                c = temp - 273.15
                f = (c * 9/5) + 32
                result = f"Celsius: {round(c, 2)}°C\nFahrenheit: {round(f, 2)}°F"
            else:
                result = "Invalid unit! Use C, F, or K."

            self.result_label.text = result
        except ValueError:
            self.result_label.text = "Enter a valid temperature."

if __name__ == '__main__':
    TempApp().run()
