#Drone UI with customisable settings and telemetry data
import tkinter as tk
from tkinter import scrolledtext
from PIL import Image, ImageTk
import random

# Global variables for drone settings
settings = {
    "Flight Mode": "Manual",
    "Speed Control": "Normal",
    "Altitude Control": "Low",
    "Camera Settings": "Auto",
    "Flight Path Planning": "Off",
    "Battery Management": "On",
    "Obstacle Avoidance": "On",
    "Emergency Stop": "Off",
    "Flight Logs": "Show"
}

def display_settings():
    # Function to display settings in a new window
    settings_window = tk.Toplevel(root)
    settings_window.title("Drone Settings")

    settings_label = tk.Label(settings_window, text="Drone Settings", font=("Helvetica", 16))
    settings_label.pack(pady=10)

    settings_frame = tk.Frame(settings_window)
    settings_frame.pack(padx=20, pady=10)

    checkboxes = []
    for i, (setting, value) in enumerate(settings.items()):
        checkbox_var = tk.BooleanVar(value=True if value == "On" else False)
        checkbox = tk.Checkbutton(settings_frame, text=setting, variable=checkbox_var, onvalue=True, offvalue=False,
                                  command=lambda v=checkbox_var, s=setting: update_setting(v, s))
        checkbox.grid(row=i, column=0, sticky="w", padx=5, pady=2)
        checkboxes.append((checkbox, checkbox_var))

def update_setting(var, setting):
    # Update the setting value
    settings[setting] = "On" if var.get() else "Off"
    print(settings)

def display_telemetry():
    # Function to display telemetry data in a new window
    telemetry_window = tk.Toplevel(root)
    telemetry_window.title("Telemetry Data")

    telemetry_label = tk.Label(telemetry_window, text="Telemetry Data", font=("Helvetica", 16))
    telemetry_label.pack(pady=10)

    telemetry_frame = tk.Frame(telemetry_window)
    telemetry_frame.pack(padx=20, pady=10)

    # Simulated telemetry data
    telemetry_data = {
        "Altitude": f"{random.randint(0, 500)} meters",
        "Speed": f"{random.randint(0, 100)} km/h",
        "Battery Level": f"{random.randint(0, 100)}%",
        "GPS Coordinates": f"({random.uniform(-180, 180):.6f}, {random.uniform(-90, 90):.6f})"
    }

    for i, (param, value) in enumerate(telemetry_data.items()):
        label = tk.Label(telemetry_frame, text=f"{param}: {value}")
        label.grid(row=i, column=0, sticky="w", padx=5, pady=2)

def activate_obstacle_avoidance():
    print("Obstacle Avoidance Activated")

def initiate_return_to_home():
    print("Returning to Home Location")

def activate_emergency_stop():
    print("Emergency Stop Activated")

def detect_environmental_hazard():
    # Simulate environmental hazard detection by generating random sensor readings
    temperature = random.randint(-20, 40)  # Simulated temperature reading in Celsius
    humidity = random.randint(0, 100)      # Simulated humidity reading in percentage
    air_quality = random.randint(0, 500)   # Simulated air quality reading (PM2.5 concentration)

    # Create a new window for displaying environmental hazard detection readings
    hazard_window = tk.Toplevel(root)
    hazard_window.title("Environmental Hazard Detection")

    # Create a text area to display the readings
    text_area = scrolledtext.ScrolledText(hazard_window, width=40, height=10, wrap=tk.WORD)
    text_area.pack(padx=10, pady=10)

    # Display simulated sensor readings in the text area
    text_area.insert(tk.END, "Environmental Hazard Detection:\n\n")
    text_area.insert(tk.END, f"Temperature: {temperature}°C\n")
    text_area.insert(tk.END, f"Humidity: {humidity}%\n")
    text_area.insert(tk.END, f"Air Quality (PM2.5): {air_quality} µg/m³\n")
    text_area.configure(state='disabled')  # Disable editing

# Create main window
root = tk.Tk()
root.title("Drone Control Panel")

# Create frames for left, middle, and right sections
left_frame = tk.Frame(root, bg="white", width=200, height=600)
left_frame.pack_propagate(False)
left_frame.pack(side="left", fill="y")

middle_frame = tk.Frame(root, bg="white", width=600, height=600)
middle_frame.pack_propagate(False)
middle_frame.pack(side="left", expand=True, fill="both")

right_frame = tk.Frame(root, bg="white", width=200, height=600)
right_frame.pack_propagate(False)
right_frame.pack(side="left", fill="y")

# Load and display map image
map_image = Image.open("bangalore_map.jpg")  # Replace "your_map_image.jpg" with the path to your map image
map_photo = ImageTk.PhotoImage(map_image)
map_label = tk.Label(middle_frame, image=map_photo)
map_label.pack(expand=True)

# Add buttons to open settings window and display telemetry on the right side
button_open_settings_window = tk.Button(right_frame, text="Open Settings", command=display_settings)
button_open_settings_window.pack(pady=10)

button_display_telemetry = tk.Button(right_frame, text="Display Telemetry", command=display_telemetry)
button_display_telemetry.pack(pady=10)

# Run the application
root.mainloop()


