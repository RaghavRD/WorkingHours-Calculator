
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup

# Function to convert HH:MM format to decimal hours
def convert_to_decimal(time_str):
    try:
        hours, minutes = map(int, time_str.split(":"))
        decimal_hours = hours + minutes / 60
        return decimal_hours
    except ValueError:
        return None

# Function to convert decimal hours to HH:MM format
def convert_to_hhmm(decimal_hours):
    hours = int(decimal_hours)
    minutes = int((decimal_hours - hours) * 60)
    return f"{hours:02}:{minutes:02}"

class WorkingHourApp(BoxLayout):
    def __init__(self, **kwargs):
        super(WorkingHourApp, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10
        self.padding = 20

        # Days worked input
        self.add_widget(Label(text='Days Worked:'))
        self.days_worked_input = TextInput(hint_text='Enter days (e.g., 4)', multiline=False)
        self.add_widget(self.days_worked_input)

        # Hours worked input
        self.add_widget(Label(text='Total Hours Worked (HH:MM):'))
        self.hours_worked_input = TextInput(hint_text='HH:MM', multiline=False)
        self.add_widget(self.hours_worked_input)

        # Calculate button
        self.calculate_button = Button(text='Calculate')
        self.calculate_button.bind(on_press=self.calculate_work_hours)
        self.add_widget(self.calculate_button)

        # Result label
        self.result_label = Label(text='')
        self.add_widget(self.result_label)

    def calculate_work_hours(self, instance):
        weekly_target_hours = 48  # Weekly target hours remain the same
        try:
            days_worked = int(self.days_worked_input.text)
            hours_worked_str = self.hours_worked_input.text

            # Convert input to decimal
            hours_worked = convert_to_decimal(hours_worked_str)
            if hours_worked is None:
                self.show_popup("Invalid Input", "Please enter time in HH:MM format.")
                return

            # Calculate remaining hours
            remaining_hours = weekly_target_hours - hours_worked
            remaining_days = 6 - days_worked

            if remaining_days > 0:
                daily_work_needed = remaining_hours / remaining_days
                remaining_hours_hhmm = convert_to_hhmm(remaining_hours)
                daily_work_needed_hhmm = convert_to_hhmm(daily_work_needed)

                self.result_label.text = (f"You have {remaining_hours_hhmm} hours left to complete this week.\n"
                                          f"Work {daily_work_needed_hhmm} hours per day for the remaining {remaining_days} days.")
            else:
                if remaining_hours > 0:
                    remaining_hours_hhmm = convert_to_hhmm(remaining_hours)
                    self.result_label.text = (f"No remaining workdays, but {remaining_hours_hhmm} hours left to complete.")
                else:
                    self.result_label.text = "You've completed your work hours for the week!"

        except ValueError:
            self.show_popup("Input Error", "Please enter valid numbers.")

    # Popup for error messages
    def show_popup(self, title, message):
        popup = Popup(title=title,
                      content=Label(text=message),
                      size_hint=(None, None), size=(300, 200))
        popup.open()


class WorkingHourCalculatorApp(App):
    def build(self):
        return WorkingHourApp()

# Run the app
if __name__ == '__main__':
    WorkingHourCalculatorApp().run()
