#Drone UI with Multiple Drone selection and settings
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Drone:
    def __init__(self, name):
        self.name = name
        self.altitude = "Low"
        self.speed = "Normal"
        self.camera_settings = "Auto"
        self.selected = False  # Initially not selected

# Global list to store drone objects
drones = [Drone("Drone 1"), Drone("Drone 2"), Drone("Drone 3")]

def display_settings():
    # Function to display settings in a new window
    settings_window = tk.Toplevel(root)
    settings_window.title("Drone Settings")
    
    settings_label = tk.Label(settings_window, text="Drone Settings", font=("Helvetica", 16))
    settings_label.pack(pady=10)
    
    settings_frame = tk.Frame(settings_window)
    settings_frame.pack(padx=20, pady=10)

    # Get the selected drone from the dropdown menu
    selected_drone = drone_combobox.get()

    # Find the corresponding Drone object
    selected_drone_obj = next((drone for drone in drones if drone.name == selected_drone), None)

    if selected_drone_obj:
        settings_data = [
            ("Drone Name:", selected_drone_obj.name),
            ("Altitude Control:", selected_drone_obj.altitude),
            ("Speed Control:", selected_drone_obj.speed),
            ("Camera Settings:", selected_drone_obj.camera_settings),
        ]

        for label_text, value in settings_data:
            label = tk.Label(settings_frame, text=label_text, width=20, anchor="w")
            label.grid(sticky="w", padx=5, pady=2)
            
            value_label = tk.Label(settings_frame, text=value, width=10, anchor="w")
            value_label.grid(row=label.grid_info()["row"], column=1, sticky="w", padx=5, pady=2)
    else:
        label = tk.Label(settings_frame, text="No drone selected", width=30, anchor="w")
        label.grid(sticky="w", padx=5, pady=2)

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
map_image = Image.open("bangalore_map.jpg")  # Replace "bangalore_map.jpg" with the path to your map image
map_photo = ImageTk.PhotoImage(map_image)
map_label = tk.Label(middle_frame, image=map_photo)
map_label.image = map_photo  # Keep a reference to prevent garbage collection
map_label.pack(expand=True)

# Add widgets to right frame (select drones)
label_select_drones = tk.Label(right_frame, text="Select Drone:", font=("Helvetica", 16))
label_select_drones.pack(pady=10)

# Create dropdown menu to select drones
drone_names = [drone.name for drone in drones]
selected_drone_var = tk.StringVar(value=drone_names[0])
drone_combobox = ttk.Combobox(right_frame, textvariable=selected_drone_var, values=drone_names, state="readonly")
drone_combobox.pack(pady=5)

button_display_selected = tk.Button(right_frame, text="Display Selected Drone", command=lambda: print("Selected Drone: " + drone_combobox.get()))
button_display_selected.pack(pady=5)

button_start_surveillance = tk.Button(right_frame, text="Start Surveillance", command=lambda: print("Starting Surveillance"))
button_start_surveillance.pack(pady=5)

button_settings = tk.Button(right_frame, text="Settings", command=display_settings)
button_settings.pack(pady=5)

# Run the application
root.mainloop()
