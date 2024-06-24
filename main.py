from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from datetime import datetime


class AppForTimePicker(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=20)

       
        self.hour_spinner = Spinner(text='Часы', values=[str(i) for i in range(1, 12)])
        self.minute_spinner = Spinner(text='Минуты', values=[f'{i:02}' for i in range(0, 60)])
        self.ampm_spinner = Spinner(text='AM/PM', values=['AM', 'PM'])

        
        self.show_time_button = Button(text='ShowTime', size_hint=(1, None), height=30)
        self.show_time_button.bind(on_press=self.show_selected_time)

        
        self.selected_time_label = Label(text='Выбранное время: ', size_hint_y=None, height=50)
        
        add_vidgets()

        return self.layout

    def show_time(self, instance):
        
        hour = self.hour_spinner.text
        minute = self.minute_spinner.text
        ampm = self.ampm_spinner.text

        
        formatted_time = f'{hour}:{minute} {ampm}'

        
        self.selected_time_label.text = f'Выбранное время: {formatted_time}'

    def add_vidgets(self, instance):
        self.layout.add_widget(self.hour_spinner)
        self.layout.add_widget(self.minute_spinner)
        self.layout.add_widget(self.ampm_spinner)
        self.layout.add_widget(self.show_time_button)
        self.layout.add_widget(self.selected_time_label)


if __name__ == '__main__':
    AppForTimePicker().run()
