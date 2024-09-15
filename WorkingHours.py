# import tkinter as tk
# from tkinter import messagebox

# def calculate_work_hours():
#     try:
#         # Get inputs from user
#         weekly_target_hours = float(target_hours_entry.get())
#         days_worked = int(days_worked_entry.get())
#         hours_worked = float(hours_worked_entry.get())

#         # Calculate remaining hours and days
#         remaining_hours = weekly_target_hours - hours_worked
#         remaining_days = 6 - days_worked
        
#         if remaining_days > 0:
#             daily_work_needed = remaining_hours / remaining_days
#             result_label.config(
#                 text=f"You have {remaining_hours:.2f} hours left to complete this week.\n"
#                      f"You need to work {daily_work_needed:.2f} hours per day for the remaining {remaining_days} days."
#             )
#         else:
#             if remaining_hours > 0:
#                 result_label.config(
#                     text=f"You have no remaining workdays, but still need to work {remaining_hours:.2f} hours."
#                 )
#             else:
#                 result_label.config(
#                     text="You've completed your work hours for the week!"
#                 )
#     except ValueError:
#         messagebox.showerror("Input Error", "Please enter valid numbers.")

# # Create the GUI window
# root = tk.Tk()
# root.title("Working Hour Calculator App")

# # Create input fields and labels
# tk.Label(root, text="Weekly Target Hours:").grid(row=0, column=0, padx=10, pady=10)
# target_hours_entry = tk.Entry(root)
# target_hours_entry.grid(row=0, column=1)
# target_hours_entry.insert(0, "48")  # Default target hours

# tk.Label(root, text="Days Worked:").grid(row=1, column=0, padx=10, pady=10)
# days_worked_entry = tk.Entry(root)
# days_worked_entry.grid(row=1, column=1)

# tk.Label(root, text="Total Hours Worked:").grid(row=2, column=0, padx=10, pady=10)
# hours_worked_entry = tk.Entry(root)
# hours_worked_entry.grid(row=2, column=1)

# # Button to calculate hours
# calculate_button = tk.Button(root, text="Calculate", command=calculate_work_hours)
# calculate_button.grid(row=3, columnspan=2, pady=20)

# # Result label to show the output
# result_label = tk.Label(root, text="")
# result_label.grid(row=4, columnspan=2, pady=10)

# # Start the GUI event loop
# root.mainloop()



# import customtkinter as ctk
# from tkinter import messagebox

# # Initialize the app window
# ctk.set_appearance_mode("dark")  # Can be set to "light" or "system" as well
# ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"

# def calculate_work_hours():
#     try:
#         # Get user inputs
#         weekly_target_hours = float(target_hours_entry.get())
#         days_worked = int(days_worked_entry.get())
#         hours_worked = float(hours_worked_entry.get())

#         # Calculate remaining hours and days
#         remaining_hours = weekly_target_hours - hours_worked
#         remaining_days = 6 - days_worked

#         if remaining_days > 0:
#             daily_work_needed = remaining_hours / remaining_days
#             result_label.configure(
#                 text=f"You have {remaining_hours:.2f} hours left to complete this week.\n"
#                      f"Work {daily_work_needed:.2f} hours per day for the remaining {remaining_days} days."
#             )
#         else:
#             if remaining_hours > 0:
#                 result_label.configure(
#                     text=f"No remaining workdays, but {remaining_hours:.2f} hours left to complete."
#                 )
#             else:
#                 result_label.configure(text="You've completed your work hours for the week!")
#     except ValueError:
#         messagebox.showerror("Input Error", "Please enter valid numbers.")

# # Create the GUI window
# app = ctk.CTk()
# app.geometry("400x400")
# app.title("Working Hour Calculator App")

# # Create input fields and labels
# label_font = ("Helvetica", 14)

# ctk.CTkLabel(app, text="Weekly Target Hours:", font=label_font).pack(pady=10)
# target_hours_entry = ctk.CTkEntry(app, width=200)
# target_hours_entry.pack()
# target_hours_entry.insert(0, "48")  # Default target hours

# ctk.CTkLabel(app, text="Days Worked:", font=label_font).pack(pady=10)
# days_worked_entry = ctk.CTkEntry(app, width=200)
# days_worked_entry.pack()

# ctk.CTkLabel(app, text="Total Hours Worked:", font=label_font).pack(pady=10)
# hours_worked_entry = ctk.CTkEntry(app, width=200)
# hours_worked_entry.pack()

# # Button to calculate hours
# calculate_button = ctk.CTkButton(app, text="Calculate", command=calculate_work_hours)
# calculate_button.pack(pady=20)

# # Result label to show the output
# result_label = ctk.CTkLabel(app, text="", font=("Helvetica", 14))
# result_label.pack(pady=20)

# # Start the app
# app.mainloop()



# import customtkinter as ctk
# from tkinter import messagebox

# # Convert HH:MM format to decimal hours
# def convert_to_decimal(time_str):
#     try:
#         hours, minutes = map(int, time_str.split(":"))
#         decimal_hours = hours + minutes / 60
#         return decimal_hours
#     except ValueError:
#         return None

# # Convert decimal hours to HH:MM format
# def convert_to_hhmm(decimal_hours):
#     hours = int(decimal_hours)
#     minutes = int((decimal_hours - hours) * 60)
#     return f"{hours:02}:{minutes:02}"

# def calculate_work_hours():
#     try:
#         # Get user inputs
#         weekly_target_hours = 48  # Weekly target hours remain the same
#         days_worked = int(days_worked_entry.get())

#         # Get the total worked hours in HH:MM format and convert to decimal
#         hours_worked_str = hours_worked_entry.get()
#         hours_worked = convert_to_decimal(hours_worked_str)

#         if hours_worked is None:
#             messagebox.showerror("Input Error", "Please enter time in HH:MM format.")
#             return

#         # Calculate remaining hours and days
#         remaining_hours = weekly_target_hours - hours_worked
#         remaining_days = 6 - days_worked

#         if remaining_days > 0:
#             daily_work_needed = remaining_hours / remaining_days

#             # Convert remaining hours and daily work needed to HH:MM format
#             remaining_hours_hhmm = convert_to_hhmm(remaining_hours)
#             daily_work_needed_hhmm = convert_to_hhmm(daily_work_needed)

#             result_label.configure(
#                 text=f"You have {remaining_hours_hhmm} hours left to complete this week.\n"
#                      f"Work {daily_work_needed_hhmm} hours per day for the remaining {remaining_days} days."
#             )
#         else:
#             if remaining_hours > 0:
#                 remaining_hours_hhmm = convert_to_hhmm(remaining_hours)
#                 result_label.configure(
#                     text=f"No remaining workdays, but {remaining_hours_hhmm} hours left to complete."
#                 )
#             else:
#                 result_label.configure(text="You've completed your work hours for the week!")
#     except ValueError:
#         messagebox.showerror("Input Error", "Please enter valid numbers.")

# # Create the GUI window
# app = ctk.CTk()
# app.geometry("400x400")
# app.title("Working Hour Calculator App")

# # Create input fields and labels
# label_font = ("Helvetica", 14)

# ctk.CTkLabel(app, text="Days Worked:", font=label_font).pack(pady=10)
# days_worked_entry = ctk.CTkEntry(app, width=200)
# days_worked_entry.pack()

# ctk.CTkLabel(app, text="Total Hours Worked (HH:MM):", font=label_font).pack(pady=10)
# hours_worked_entry = ctk.CTkEntry(app, width=200, placeholder_text="HH:MM")
# hours_worked_entry.pack()

# # Button to calculate hours
# calculate_button = ctk.CTkButton(app, text="Calculate", command=calculate_work_hours)
# calculate_button.pack(pady=20)

# # Result label to show the output
# result_label = ctk.CTkLabel(app, text="", font=("Helvetica", 14))
# result_label.pack(pady=20)

# # Start the app
# app.mainloop()


# import customtkinter as ctk
# from tkinter import messagebox

# # Convert HH:MM format to decimal hours
# def convert_to_decimal(time_str):
#     try:
#         hours, minutes = map(int, time_str.split(":"))
#         decimal_hours = hours + minutes / 60
#         return decimal_hours
#     except ValueError:
#         return None

# # Convert decimal hours to HH:MM format
# def convert_to_hhmm(decimal_hours):
#     hours = int(decimal_hours)
#     minutes = int((decimal_hours - hours) * 60)
#     return f"{hours:02}:{minutes:02}"

# # This function calculates the total hours worked for multiple days
# def calculate_total_worked_hours(days):
#     total_hours = 0
#     for day in range(1, days + 1):
#         day_hours_str = ctk.CTkInputDialog(text=f"Enter hours worked for Day {day} (HH:MM format):", title=f"Day {day}").get_input()
#         day_hours = convert_to_decimal(day_hours_str)
        
#         if day_hours is None:
#             messagebox.showerror("Input Error", f"Invalid input for Day {day}. Please enter time in HH:MM format.")
#             return None
        
#         total_hours += day_hours
#     return total_hours

# def calculate_work_hours():
#     try:
#         # Get user inputs
#         weekly_target_hours = 48  # Weekly target hours remain the same
#         days_worked = int(days_worked_entry.get())

#         # Ask for the hours worked each day and calculate the total hours
#         total_hours_worked = calculate_total_worked_hours(days_worked)

#         if total_hours_worked is None:
#             return  # Exit the function if there's an invalid input

#         # Calculate remaining hours and days
#         remaining_hours = weekly_target_hours - total_hours_worked
#         remaining_days = 6 - days_worked

#         if remaining_days > 0:
#             daily_work_needed = remaining_hours / remaining_days

#             # Convert remaining hours and daily work needed to HH:MM format
#             remaining_hours_hhmm = convert_to_hhmm(remaining_hours)
#             daily_work_needed_hhmm = convert_to_hhmm(daily_work_needed)

#             result_label.configure(
#                 text=f"You have {remaining_hours_hhmm} hours left to complete this week.\n"
#                      f"Work {daily_work_needed_hhmm} hours per day for the remaining {remaining_days} days."
#             )
#         else:
#             if remaining_hours > 0:
#                 remaining_hours_hhmm = convert_to_hhmm(remaining_hours)
#                 result_label.configure(
#                     text=f"No remaining workdays, but {remaining_hours_hhmm} hours left to complete."
#                 )
#             else:
#                 result_label.configure(text="You've completed your work hours for the week!")
#     except ValueError:
#         messagebox.showerror("Input Error", "Please enter valid numbers.")

# # Create the GUI window
# app = ctk.CTk()
# app.geometry("400x400")
# app.title("Working Hours")
# app.iconbitmap("working-hours.ico")

# # Create input fields and labels
# label_font = ("Helvetica", 14)

# ctk.CTkLabel(app, text="Days Worked:", font=label_font).pack(pady=10)
# days_worked_entry = ctk.CTkEntry(app, width=200)
# days_worked_entry.pack()

# # Button to calculate hours
# calculate_button = ctk.CTkButton(app, text="Calculate", command=calculate_work_hours)
# calculate_button.pack(pady=20)

# # Result label to show the output
# result_label = ctk.CTkLabel(app, text="", font=("Helvetica", 14))
# result_label.pack(pady=20)

# # Start the app
# app.mainloop()



# import customtkinter as ctk
# from tkinter import messagebox
# import sys

# # Set default appearance mode and color theme
# ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
# ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "dark-blue", "green"

# # Convert HH:MM format to decimal hours
# def convert_to_decimal(time_str):
#     try:
#         hours, minutes = map(int, time_str.strip().split(":"))
#         decimal_hours = hours + minutes / 60
#         return decimal_hours
#     except ValueError:
#         return None

# # Convert decimal hours to HH:MM format
# def convert_to_hhmm(decimal_hours):
#     total_minutes = int(round(decimal_hours * 60))
#     hours, minutes = divmod(total_minutes, 60)
#     return f"{hours:02}:{minutes:02}"

# class WorkingHourApp(ctk.CTk):
#     def __init__(self):
#         super().__init__()

#         self.title("Working Hour Calculator App")
#         self.geometry("500x600")

#         # Add custom icon to the window (if needed)
#         # self.iconbitmap("path/to/your/icon.ico")

#         # Main frame
#         self.main_frame = ctk.CTkFrame(self)
#         self.main_frame.pack(pady=20, padx=20, fill="both", expand=True)

#         # Title label
#         self.label_font = ctk.CTkFont(size=14)
#         self.title_label = ctk.CTkLabel(self.main_frame, text="Working Hour Calculator", font=ctk.CTkFont(size=18, weight="bold"))
#         self.title_label.pack(pady=10)

#         # Days worked input
#         self.days_worked_label = ctk.CTkLabel(self.main_frame, text="Days Worked:", font=self.label_font)
#         self.days_worked_label.pack(pady=5)
#         self.days_worked_entry = ctk.CTkEntry(self.main_frame, width=200)
#         self.days_worked_entry.pack()

#         # Button to generate daily input fields
#         self.generate_button = ctk.CTkButton(self.main_frame, text="Enter Daily Hours", command=self.generate_daily_inputs)
#         self.generate_button.pack(pady=10)

#         # Frame to hold daily hour inputs
#         self.daily_hours_frame = ctk.CTkFrame(self.main_frame)
#         self.daily_hours_entries = []  # To hold references to daily input entries

#         # Button to calculate hours
#         self.calculate_button = ctk.CTkButton(self.main_frame, text="Calculate", command=self.calculate_work_hours)
#         # Initially disabled
#         self.calculate_button.pack(pady=10)
#         self.calculate_button.configure(state="disabled")

#         # Result label to show the output
#         self.result_label = ctk.CTkLabel(self.main_frame, text="", font=self.label_font)
#         self.result_label.pack(pady=10)

#         # Theme switch button
#         self.theme_switch_button = ctk.CTkButton(self.main_frame, text="Switch Theme", command=self.switch_theme)
#         self.theme_switch_button.pack(pady=10)

#     def switch_theme(self):
#         current_mode = ctk.get_appearance_mode()
#         if current_mode == "Light":
#             ctk.set_appearance_mode("Dark")
#         else:
#             ctk.set_appearance_mode("Light")

#     def generate_daily_inputs(self):
#         try:
#             days_worked = int(self.days_worked_entry.get())
#             if days_worked < 1 or days_worked > 6:
#                 messagebox.showerror("Input Error", "Days worked must be between 1 and 6.")
#                 return
#         except ValueError:
#             messagebox.showerror("Input Error", "Please enter a valid number for days worked.")
#             return

#         # Clear previous entries if any
#         for widget in self.daily_hours_frame.winfo_children():
#             widget.destroy()
#         self.daily_hours_entries.clear()

#         # Show the daily hours frame
#         self.daily_hours_frame.pack(pady=10)

#         # Create input fields for each day
#         for day in range(1, days_worked + 1):
#             label = ctk.CTkLabel(self.daily_hours_frame, text=f"Hours worked on Day {day} (HH:MM):", font=self.label_font)
#             label.pack(pady=5)
#             entry = ctk.CTkEntry(self.daily_hours_frame, width=200, placeholder_text="HH:MM")
#             entry.pack()
#             self.daily_hours_entries.append(entry)

#         # Enable the calculate button
#         self.calculate_button.configure(state="normal")

#     def calculate_work_hours(self):
#         weekly_target_hours = 48  # Weekly target hours remain the same

#         total_hours_worked = 0
#         for idx, entry in enumerate(self.daily_hours_entries):
#             day_hours_str = entry.get()
#             day_hours = convert_to_decimal(day_hours_str)
#             if day_hours is None:
#                 messagebox.showerror("Input Error", f"Invalid input for Day {idx + 1}. Please enter time in HH:MM format.")
#                 return
#             total_hours_worked += day_hours

#         days_worked = len(self.daily_hours_entries)
#         remaining_hours = weekly_target_hours - total_hours_worked
#         remaining_days = 6 - days_worked

#         if remaining_hours < 0:
#             remaining_hours = 0  # Avoid negative remaining hours

#         if remaining_days > 0:
#             daily_work_needed = remaining_hours / remaining_days
#             remaining_hours_hhmm = convert_to_hhmm(remaining_hours)
#             daily_work_needed_hhmm = convert_to_hhmm(daily_work_needed)

#             self.result_label.configure(
#                 text=f"You have {remaining_hours_hhmm} hours left to complete this week.\n"
#                      f"Work {daily_work_needed_hhmm} hours per day for the remaining {remaining_days} days."
#             )
#         else:
#             if remaining_hours > 0:
#                 remaining_hours_hhmm = convert_to_hhmm(remaining_hours)
#                 self.result_label.configure(
#                     text=f"No remaining workdays, but {remaining_hours_hhmm} hours left to complete."
#                 )
#             else:
#                 self.result_label.configure(text="You've completed your work hours for the week!")

# if __name__ == "__main__":
#     app = WorkingHourApp()
#     app.mainloop()




# import customtkinter as ctk
# from tkinter import messagebox

# # Convert HH:MM format to decimal hours
# def convert_to_decimal(time_str):
#     try:
#         hours, minutes = map(int, time_str.split(":"))
#         decimal_hours = hours + minutes / 60
#         return decimal_hours
#     except ValueError:
#         return None

# # Convert decimal hours to HH:MM format
# def convert_to_hhmm(decimal_hours):
#     hours = int(decimal_hours)
#     minutes = int((decimal_hours - hours) * 60)
#     return f"{hours:02}:{minutes:02}"

# def calculate_work_hours():
#     try:
#         weekly_target_hours = 48  # Weekly target hours remain the same
#         days_worked = int(days_worked_entry.get())
#         total_hours_worked = 0

#         # Get the hours worked for each day
#         for i in range(1, days_worked + 1):
#             day_hours_str = day_entries[i - 1].get()
#             day_hours = convert_to_decimal(day_hours_str)

#             if day_hours is None:
#                 messagebox.showerror("Input Error", f"Invalid input for Day {i}. Please enter time in HH:MM format.")
#                 return
            
#             total_hours_worked += day_hours

#         remaining_hours = weekly_target_hours - total_hours_worked
#         remaining_days = 6 - days_worked

#         if remaining_days > 0:
#             daily_work_needed = remaining_hours / remaining_days

#             remaining_hours_hhmm = convert_to_hhmm(remaining_hours)
#             daily_work_needed_hhmm = convert_to_hhmm(daily_work_needed)

#             result_label.configure(
#                 text=f"You have {remaining_hours_hhmm} hours left to complete this week.\n"
#                      f"Work {daily_work_needed_hhmm} hours per day for the remaining {remaining_days} days."
#             )
#         else:
#             if remaining_hours > 0:
#                 remaining_hours_hhmm = convert_to_hhmm(remaining_hours)
#                 result_label.configure(
#                     text=f"No remaining workdays, but {remaining_hours_hhmm} hours left to complete."
#                 )
#             else:
#                 result_label.configure(text="You've completed your work hours for the week!")
#     except ValueError:
#         messagebox.showerror("Input Error", "Please enter valid numbers.")

# def show_day_inputs():
#     try:
#         days_worked = int(days_worked_entry.get())
#         for widget in day_frame.winfo_children():
#             widget.destroy()  # Clear the previous inputs if they exist

#         # Dynamically create input fields for each day worked
#         for i in range(days_worked):
#             label = ctk.CTkLabel(day_frame, text=f"Hours Worked on Day {i + 1} (HH:MM):", font=label_font)
#             label.grid(row=i, column=0, pady=5)
#             entry = ctk.CTkEntry(day_frame, width=150)
#             entry.grid(row=i, column=1, pady=5)
#             day_entries.append(entry)

#     except ValueError:
#         messagebox.showerror("Input Error", "Please enter a valid number of days worked.")

# # Toggle between light and dark themes
# def switch_theme():
#     if ctk.get_appearance_mode() == "Dark":
#         ctk.set_appearance_mode("Light")
#     else:
#         ctk.set_appearance_mode("Dark")

# # Create the GUI window
# app = ctk.CTk()
# app.geometry("470x550")
# app.title("Working Hour Calculator App")

# # Add custom icon to the window
# # icon_image = ctk.CTkImage(file="path/to/your/icon.png")
# # app.iconphoto(False, icon_image)

# # Add a button to toggle between light and dark themes
# theme_button = ctk.CTkButton(app, text="Toggle Theme", command=switch_theme)
# theme_button.pack(pady=10)

# # Create input fields and labels
# label_font = ("Helvetica", 14)
# ctk.CTkLabel(app, text="Days Worked:", font=label_font).pack(pady=10)
# days_worked_entry = ctk.CTkEntry(app, width=150)
# days_worked_entry.pack()

# # Button to show daily working hour input fields
# show_button = ctk.CTkButton(app, text="Show Day Inputs", command=show_day_inputs)
# show_button.pack(pady=10)

# # Frame to hold dynamically created day input fields
# day_frame = ctk.CTkFrame(app)
# day_frame.pack(pady=20)
# day_entries = []

# # Button to calculate hours
# calculate_button = ctk.CTkButton(app, text="Calculate", command=calculate_work_hours)
# calculate_button.pack(pady=20)

# # Result label to show the output
# result_label = ctk.CTkLabel(app, text="", font=("Helvetica", 14))
# result_label.pack(pady=20)

# # Start the app
# app.mainloop()



import customtkinter as ctk
from tkinter import messagebox

# Convert HH:MM format to decimal hours
def convert_to_decimal(time_str):
    try:
        hours, minutes = map(int, time_str.strip().split(":"))
        decimal_hours = hours + minutes / 60
        return decimal_hours
    except ValueError:
        return None

# Convert decimal hours to HH:MM format
def convert_to_hhmm(decimal_hours):
    total_minutes = int(round(decimal_hours * 60))
    hours, minutes = divmod(total_minutes, 60)
    return f"{hours:02}:{minutes:02}"

class WorkingHourApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Working Hours App")
        self.geometry("500x600")

        # Main frame
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Title label
        self.label_font = ctk.CTkFont(size=14)
        self.title_label = ctk.CTkLabel(self.main_frame, text="⌚ Working Hour Calculator", font=ctk.CTkFont(size=18, weight="bold"))
        self.title_label.pack(pady=10)

        # Days worked input
        self.days_worked_label = ctk.CTkLabel(self.main_frame, text="Worked Days:", font=self.label_font)
        self.days_worked_label.pack(pady=5)
        self.days_worked_entry = ctk.CTkEntry(self.main_frame, width=200)
        self.days_worked_entry.pack()

        # Days off input
        self.days_off_label = ctk.CTkLabel(self.main_frame, text="Off Days:", font=self.label_font)
        self.days_off_label.pack(pady=5)
        self.days_off_entry = ctk.CTkEntry(self.main_frame, width=200)
        self.days_off_entry.pack()

        # Button to generate daily input fields
        self.generate_button = ctk.CTkButton(self.main_frame, text="Enter Daily Hours", command=self.generate_daily_inputs)
        self.generate_button.pack(pady=10)

        # Frame to hold daily hour inputs
        self.daily_hours_frame = ctk.CTkFrame(self.main_frame)
        self.daily_hours_entries = []  # To hold references to daily input entries

        # Button to calculate hours
        self.calculate_button = ctk.CTkButton(self.main_frame, text="Calculate", command=self.calculate_work_hours)
        self.calculate_button.pack(pady=10)
        self.calculate_button.configure(state="disabled")

        # Result label to show the output
        self.result_label = ctk.CTkLabel(self.main_frame, text="", font=self.label_font)
        self.result_label.pack(pady=10)

        # Theme switch button
        self.theme_switch_button = ctk.CTkButton(self.main_frame, text="Switch Theme", command=self.switch_theme)
        self.theme_switch_button.pack(pady=10)

    def switch_theme(self):
        current_mode = ctk.get_appearance_mode()
        if current_mode == "Light":
            ctk.set_appearance_mode("Dark")
        else:
            ctk.set_appearance_mode("Light")

    def generate_daily_inputs(self):
        try:
            days_worked = int(self.days_worked_entry.get())
            days_off = int(self.days_off_entry.get())

            # Ensure valid inputs
            if days_worked < 1 or days_worked > 6:
                messagebox.showerror("Working Hours App", "Days worked must be between 1 and 6.")
                return
            if days_off < 0 or days_off > (6 - days_worked):
                messagebox.showerror("Working Hours App", f"Days off must be between 0 and {6 - days_worked}.")
                return
        except ValueError:
            messagebox.showerror("Working Hours App", "Please enter valid numbers for days worked and days off.")
            return

        # Clear previous entries if any
        for widget in self.daily_hours_frame.winfo_children():
            widget.destroy()
        self.daily_hours_entries.clear()

        # Show the daily hours frame
        self.daily_hours_frame.pack(pady=10)

        # Create input fields for each day
        for day in range(1, days_worked + 1):
            label = ctk.CTkLabel(self.daily_hours_frame, text=f"Hours worked on Day {day} (HH:MM):", font=self.label_font)
            label.pack(pady=5)
            entry = ctk.CTkEntry(self.daily_hours_frame, width=200, placeholder_text="HH:MM")
            entry.pack()
            self.daily_hours_entries.append(entry)

        # Enable the calculate button
        self.calculate_button.configure(state="normal")

    def calculate_work_hours(self):
        try:
            days_worked = int(self.days_worked_entry.get())
            days_off = int(self.days_off_entry.get())
        except ValueError:
            messagebox.showerror("Working Hours App", "Please enter valid numbers for days worked and days off.")
            return

        # Total weekly target is adjusted by days off (assume 8 hours/day)
        weekly_target_hours = 48 - (days_off * 8)

        total_hours_worked = 0
        for i, entry in enumerate(self.daily_hours_entries):
            try:
                day_hours_str = entry.get()
                day_hours = convert_to_decimal(day_hours_str)
                if day_hours is None:
                    messagebox.showerror("Working Hours App", f"Invalid input for Day {i + 1}. Please enter time in HH:MM format.")
                    return
                total_hours_worked += day_hours
            except Exception as e:
                print(f"Error processing entry {i}: {e}")  # Debugging print
                messagebox.showerror("Error", f"An unexpected error occurred: {e}")
                return

        remaining_hours = weekly_target_hours - total_hours_worked
        remaining_days = 6 - days_worked - days_off  # Subtract days worked and days off from 6

        if remaining_hours < 0:
            remaining_hours = 0  # Avoid negative remaining hours

        if remaining_days > 0:
            daily_work_needed = remaining_hours / remaining_days
            remaining_hours_hhmm = convert_to_hhmm(remaining_hours)
            daily_work_needed_hhmm = convert_to_hhmm(daily_work_needed)

            self.result_label.configure(
                text=f"You have {remaining_hours_hhmm} hours left to complete this week.\n"
                     f"Work {daily_work_needed_hhmm} hours per day for the remaining {remaining_days} days."
            )
        else:
            if remaining_hours > 0:
                remaining_hours_hhmm = convert_to_hhmm(remaining_hours)
                self.result_label.configure(
                    text=f"No remaining workdays, but {remaining_hours_hhmm} hours left to complete."
                )
            else:
                self.result_label.configure(text="You've completed your work hours for the week!")

if __name__ == "__main__":
    app = WorkingHourApp()
    app.mainloop()
