#Combined Drone UI 1.0
import tkinter as tk
import webbrowser
import folium
from folium import plugins
from PIL import Image, ImageTk
import random
from tkinter import scrolledtext
from cefpython3 import cefpython as cef
import os
from tkhtmlview import HTMLLabel
import sys


# Global variables for drone settings
flight_mode = "Manual"
speed = "Normal"
altitude = "Low"
camera_settings = "Auto"
flight_path_planning = "Off"
battery_management = "On"
obstacle_avoidance = "On"
emergency_stop = "Off"
flight_logs = "Show"

# Global variables to track Shift and right-click status
shift_pressed = False
right_clicked = False

# Global variables to store the pins
pins = []

def on_left_click(event):
    global m
    if hasattr(event, 'x') and hasattr(event, 'y'):  # Check if event object has x and y attributes
        lat, lon = m.map(event.x, event.y)
        if len(pins) < 2:
            pins.append([lat, lon])
            folium.Marker([lat, lon], popup='Pin', icon=folium.Icon(color='green')).add_to(m)
            if len(pins) == 2:
                draw_polyline()

def on_right_click(event):
    global shift_pressed, right_clicked, m
    if shift_pressed:
        right_clicked = True
        if hasattr(event, 'x') and hasattr(event, 'y'):  # Check if event object has x and y attributes
            lat, lon = m.map(event.x, event.y)
            if len(pins) < 2:
                pins.append([lat, lon])
                if len(pins) == 2:
                    draw_polyline()

def on_shift_down(event):
    global shift_pressed
    shift_pressed = True

def on_shift_up(event):
    global shift_pressed
    shift_pressed = False

def draw_polyline():
    global pins, m
    if len(pins) == 2:
        polyline_points = [(pins[0][0], pins[0][1]), (pins[1][0], pins[1][1])]
        folium.PolyLine(polyline_points, color="red", weight=2.5, opacity=1).add_to(m)
        m.save('map.html')
        webbrowser.open('map.html')

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

def open_obstacle_avoidance_window():
    # Create a new window for obstacle avoidance settings
    avoidance_window = tk.Toplevel(root)
    avoidance_window.title("Obstacle Avoidance Settings")

    # Add widgets for obstacle avoidance settings
    label_avoidance = tk.Label(avoidance_window, text="Obstacle Avoidance Settings")
    label_avoidance.pack()

def open_return_to_home_window():
    # Create a new window for return-to-home settings
    return_to_home_window = tk.Toplevel(root)
    return_to_home_window.title("Return-to-Home Settings")

    # Add widgets for return-to-home settings
    label_return_home = tk.Label(return_to_home_window, text="Return-to-Home Settings")
    label_return_home.pack()

def open_emergency_stop_window():
    # Create a new window for emergency stop settings
    emergency_stop_window = tk.Toplevel(root)
    emergency_stop_window.title("Emergency Stop Settings")

    # Add widgets for emergency stop settings
    label_emergency_stop = tk.Label(emergency_stop_window, text="Emergency Stop Settings")
    label_emergency_stop.pack()

# Create main window
def close_cef():
    if not cef.GetAppSetting("external_message_pump"):
        cef.QuitMessageLoop()
    cef.Shutdown()

# Initialize CEF
def init_cef():
    sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
    settings = {
        "external_message_pump": True,  # Tkinter message loop integration
    }
    cef.Initialize(settings=settings)
    cef.CreateBrowser()

# Create main window
root = tk.Tk()
root.title("Surveillance Drone Application")

# Get screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set minimum window size
root.minsize(800, 600)

# Create frames for left, middle, and right sections
left_frame = tk.Frame(root, bg="gray", width=200, height=600)
left_frame.pack_propagate(False)
left_frame.pack(side="left", fill="y")

middle_frame = tk.Frame(root, bg="white", width=800, height=600)
middle_frame.pack_propagate(False)
middle_frame.pack(side="left", expand=True, fill="both")

right_frame = tk.Frame(root, bg="lightgray", width=200, height=600)
right_frame.pack_propagate(False)
right_frame.pack(side="left", fill="y")

# Add widgets to left frame (drone cameras)
label_drone_cameras = tk.Label(left_frame, text="Drone Cameras", font=("Helvetica", 16))
label_drone_cameras.pack(pady=10)

# Load and display map image
map_image=Image.open("C:\\Users\\ChrisJohn\\Desktop\\DAISY\\APPlICATION\\MAP\\bangalore_map.jpg")
map_photo = ImageTk.PhotoImage(map_image)
map_label = tk.Label(middle_frame, image=map_photo)
map_label.image = map_photo  # Keep a reference to prevent garbage collection
map_label.pack(expand=True)

# Add widgets to right frame (select drones)
label_select_drones = tk.Label(right_frame, text="Selected Drone: Drone 1", font=("Helvetica", 16))
label_select_drones.pack(pady=10)

button_display_selected = tk.Button(right_frame, text="Display Selected Drone", command=lambda: print("Selected Drone: Drone 1"))
button_display_selected.pack(pady=5)

button_start_surveillance = tk.Button(right_frame, text="Start Surveillance", command=lambda: print("Starting Surveillance"))
button_start_surveillance.pack(pady=5)

# Button to activate obstacle avoidance
button_obstacle_avoidance = tk.Button(right_frame, text="Activate Obstacle Avoidance", command=activate_obstacle_avoidance)
button_obstacle_avoidance.pack(pady=5)

# Button to initiate return to home
button_return_to_home = tk.Button(right_frame, text="Initiate Return to Home", command=initiate_return_to_home)
button_return_to_home.pack(pady=5)

# Button to activate emergency stop
button_emergency_stop = tk.Button(right_frame, text="Activate Emergency Stop", command=activate_emergency_stop)
button_emergency_stop.pack(pady=5)

# Button to detect environmental hazard
button_detect_hazard = tk.Button(right_frame, text="Detect Environmental Hazard", command=detect_environmental_hazard)
button_detect_hazard.pack(pady=5)

button_settings = tk.Button(right_frame, text="Settings", command=display_settings)
button_settings.pack(pady=5)

# Create the map
m = folium.Map(location=[12.9716, 77.5946], zoom_start=12)
marker_cluster = plugins.MarkerCluster().add_to(m)

# Bind mouse events
root.bind("<Shift_L>", on_shift_down)
root.bind("<Shift_R>", on_shift_down)
root.bind("<KeyRelease-Shift_L>", on_shift_up)
root.bind("<KeyRelease-Shift_R>", on_shift_up)
m.add_child(folium.ClickForMarker(popup='Add pin'))
m.add_child(folium.LatLngPopup())
root.bind("<Button-1>", on_left_click)
root.bind("<Button-3>", on_right_click)

# Create MiniMap
mini_map = plugins.MiniMap(toggle_display=True).add_to(m)
# Save map to HTML
m.save('map.html')

# Load and display the map HTML content in the middle_frame using HTMLLabel
with open('map.html', 'r') as file:
    html_content = file.read()
html_label = HTMLLabel(middle_frame, html=html_content, width=100, height=50)
html_label.pack(fill="both", expand=True)

# Run the application
root.mainloop()
