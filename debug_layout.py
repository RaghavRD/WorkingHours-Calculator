import customtkinter as ctk
import sys
import os

# Add current directory to path so we can import WorkingHours
sys.path.append(os.getcwd())

try:
    from WorkingHours import WorkingHourApp
except ImportError:
    # If running from a different directory, adjust path
    sys.path.append(os.path.join(os.getcwd(), "WorkingHours-Calculator"))
    from WorkingHours import WorkingHourApp

def test_logic():
    app = WorkingHourApp()
    
    # Simulate inputs
    app.days_worked_entry.insert(0, "4")
    app.days_off_entry.insert(0, "1")
    
    # Trigger generation
    app.generate_daily_inputs()
    
    # Check count
    count = len(app.daily_hours_entries)
    print(f"DEBUG: Created {count} daily input entries.")
    
    if count == 4:
        print("DEBUG: Logic is CORRECT. Issue is likely UI Layout/Overflow.")
    else:
        print("DEBUG: Logic is INCORRECT.")

    # We don't need to run the mainloop for this logic check
    app.destroy()

if __name__ == "__main__":
    test_logic()
