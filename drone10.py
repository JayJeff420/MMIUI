#Dynamic Map
import tkinter as tk
from tkinter import scrolledtext
import webbrowser
import folium
from folium import plugins
import random

# Global variables to track Shift and right-click status
shift_pressed = False
right_clicked = False

# Global variables to store the pins
pins = []

def on_left_click(event):
    lat, lon = event.lat, event.lng
    if len(pins) < 2:
        pins.append([lat, lon])
        folium.Marker([lat, lon], popup='Pin', icon=folium.Icon(color='green')).add_to(marker_cluster)
        if len(pins) == 2:
            draw_polyline()

def on_right_click(event):
    global right_clicked
    if shift_pressed:
        right_clicked = True
        lat, lon = event.lat, event.lng
        if len(pins) < 2:
            pins.append([lat, lon])
            if len(pins) == 2:
                draw_polyline()
    else:
        detect_environmental_hazard()

def on_shift_down(event):
    global shift_pressed
    shift_pressed = True

def on_shift_up(event):
    global shift_pressed
    shift_pressed = False

def draw_polyline():
    global pins
    if len(pins) == 2:
        polyline_points = [(pins[0][0], pins[0][1]), (pins[1][0], pins[1][1])]
        folium.PolyLine(polyline_points, color="red", weight=2.5, opacity=1).add_to(m)
        m.save('map.html')
        webbrowser.open('map.html')

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

def display_safety_features():
    # Create a new window for safety features
    safety_window = tk.Toplevel(root)
    safety_window.title("Safety Features")

    # Add buttons for safety features
    button_obstacle_avoidance = tk.Button(safety_window, text="Activate Obstacle Avoidance", command=activate_obstacle_avoidance)
    button_obstacle_avoidance.pack(pady=5)

    button_return_to_home = tk.Button(safety_window, text="Initiate Return to Home", command=initiate_return_to_home)
    button_return_to_home.pack(pady=5)

    button_emergency_stop = tk.Button(safety_window, text="Activate Emergency Stop", command=activate_emergency_stop)
    button_emergency_stop.pack(pady=5)

    button_detect_hazard = tk.Button(safety_window, text="Detect Environmental Hazard", command=detect_environmental_hazard)
    button_detect_hazard.pack(pady=5)

def activate_obstacle_avoidance():
    print("Obstacle Avoidance Activated")

def initiate_return_to_home():
    print("Returning to Home Location")

def activate_emergency_stop():
    print("Emergency Stop Activated")

root = tk.Tk()
root.title("Interactive Map")

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

root.mainloop()
