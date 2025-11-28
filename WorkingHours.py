import customtkinter as ctk
from tkinter import messagebox

# Configuration for Modern Minimalist Theme
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("dark-blue")

# Custom Colors
ACCENT_COLOR = "#20B2AA"  # Light Sea Green / Teal
TEXT_COLOR = "#FFFFFF"
SUBTLE_TEXT_COLOR = "#A0A0A0"
ENTRY_BG_COLOR = "transparent"
ENTRY_BORDER_COLOR = "#404040"

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

        self.title("Working Hours")
        self.geometry("450x650")
        self.resizable(True, True)

        # Main container - Static Frame initially
        self.main_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.main_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # --- Header ---
        self.title_label = ctk.CTkLabel(
            self.main_frame, 
            text="Working Hours", 
            font=ctk.CTkFont(family="Roboto", size=32, weight="normal"),
            text_color=TEXT_COLOR
        )
        self.title_label.pack(pady=(20, 40))

        # --- Inputs ---
        self.input_container = ctk.CTkFrame(self.main_frame, fg_color="transparent")
        self.input_container.pack(fill="x", pady=(0, 30))

        # Days Worked
        self.create_minimal_input(self.input_container, "Days Worked", "days_worked_entry")
        
        # Days Off
        self.create_minimal_input(self.input_container, "Days Off", "days_off_entry")

        # --- Dynamic Daily Inputs Area ---
        self.daily_inputs_button = ctk.CTkButton(
            self.main_frame,
            text="Enter Daily Hours",
            command=self.generate_daily_inputs,
            fg_color="transparent",
            border_width=1,
            border_color=SUBTLE_TEXT_COLOR,
            text_color=SUBTLE_TEXT_COLOR,
            hover_color="#333333",
            height=30,
            corner_radius=15,
            font=ctk.CTkFont(size=12)
        )
        self.daily_inputs_button.pack(pady=(0, 20))

        # Placeholders for dynamic widgets
        self.scroll_area = None
        self.daily_hours_entries = []
        self.result_label = None

    def create_minimal_input(self, parent, label_text, attr_name):
        frame = ctk.CTkFrame(parent, fg_color="transparent")
        frame.pack(fill="x", pady=10)
        
        label = ctk.CTkLabel(
            frame, 
            text=label_text, 
            font=ctk.CTkFont(size=14, weight="normal"),
            text_color=SUBTLE_TEXT_COLOR,
            anchor="w"
        )
        label.pack(fill="x")

        entry = ctk.CTkEntry(
            frame,
            width=200,
            height=35,
            fg_color=ENTRY_BG_COLOR,
            border_width=0,
            text_color=TEXT_COLOR,
            font=ctk.CTkFont(size=16)
        )
        # Add a custom bottom border using a separator or frame
        bottom_border = ctk.CTkFrame(frame, height=1, fg_color=ENTRY_BORDER_COLOR)
        
        entry.pack(fill="x")
        bottom_border.pack(fill="x")
        
        setattr(self, attr_name, entry)

    def generate_daily_inputs(self):
        try:
            days_worked_str = self.days_worked_entry.get()
            days_off_str = self.days_off_entry.get()

            if not days_worked_str:
                messagebox.showerror("Input Error", "Please enter days worked.")
                return
            
            days_worked = int(days_worked_str)
            days_off = int(days_off_str) if days_off_str else 0

            if days_worked < 1 or days_worked > 6:
                messagebox.showerror("Input Error", "Days worked must be between 1 and 6.")
                return
            if days_off < 0 or days_off > (6 - days_worked):
                messagebox.showerror("Input Error", f"Days off must be between 0 and {6 - days_worked}.")
                return
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid numbers.")
            return

        # Clear previous scroll area if it exists
        if self.scroll_area:
            self.scroll_area.destroy()
        self.daily_hours_entries.clear()

        # Create new Scrollable Frame for inputs and results
        self.scroll_area = ctk.CTkScrollableFrame(self.main_frame, fg_color="transparent")
        self.scroll_area.pack(fill="both", expand=True, pady=10)

        for day in range(1, days_worked + 1):
            frame = ctk.CTkFrame(self.scroll_area, fg_color="transparent")
            frame.pack(fill="x", pady=5)
            
            lbl = ctk.CTkLabel(frame, text=f"Day {day}", width=60, anchor="w", text_color=SUBTLE_TEXT_COLOR)
            lbl.pack(side="left")
            
            entry = ctk.CTkEntry(
                frame, 
                placeholder_text="HH:MM",
                fg_color="transparent",
                border_width=0,
                text_color=TEXT_COLOR,
                height=30
            )
            border = ctk.CTkFrame(frame, height=1, fg_color=ENTRY_BORDER_COLOR)
            
            entry.pack(side="left", fill="x", expand=True)
            border.place(relx=0, rely=1.0, relwidth=1.0, anchor="sw") 
            
            self.daily_hours_entries.append(entry)

        # --- Calculate Button ---
        self.calculate_button = ctk.CTkButton(
            self.scroll_area,
            text="CALCULATE",
            command=self.calculate_work_hours,
            fg_color="transparent",
            border_width=2,
            border_color=ACCENT_COLOR,
            text_color=ACCENT_COLOR,
            hover_color="#262626",
            height=50,
            corner_radius=25,
            font=ctk.CTkFont(size=14, weight="bold")
        )
        self.calculate_button.pack(pady=(20, 30), fill="x")

        # --- Result Area ---
        self.result_label = ctk.CTkLabel(
            self.scroll_area,
            text="",
            font=ctk.CTkFont(size=18, weight="normal"),
            text_color=TEXT_COLOR,
            justify="center"
        )
        self.result_label.pack(pady=10)

    def calculate_work_hours(self):
        try:
            days_worked = int(self.days_worked_entry.get())
            days_off_str = self.days_off_entry.get()
            days_off = int(days_off_str) if days_off_str else 0
        except ValueError:
            return

        weekly_target = 48 - (days_off * 8)
        total_worked = 0

        for entry in self.daily_hours_entries:
            val = convert_to_decimal(entry.get())
            if val is None:
                messagebox.showerror("Input Error", "Invalid time format. Use HH:MM")
                return
            total_worked += val

        remaining = max(0, weekly_target - total_worked)
        remaining_days = 6 - days_worked - days_off

        rem_str = convert_to_hhmm(remaining)
        
        if remaining_days > 0:
            daily_needed = remaining / remaining_days
            daily_str = convert_to_hhmm(daily_needed)
            result_text = f"{rem_str} Hours Left\n\nTarget: {daily_str} / day"
        else:
            if remaining > 0:
                result_text = f"{rem_str} Hours Left\n(No days remaining)"
            else:
                result_text = "Goal Reached! 🎉"

        if self.result_label:
            self.result_label.configure(text=result_text)

if __name__ == "__main__":
    app = WorkingHourApp()
    app.mainloop()
