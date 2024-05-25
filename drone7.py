#Drone UI with flight path
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
        self.waypoints = []  # List to store waypoints

# Global list to store drone objects
drones = [Drone("Drone 1"), Drone("Drone 2"), Drone("Drone 3")]

# Function to handle click events on the map
def on_map_click(event):
    # Get the coordinates of the click event
    x, y = event.x, event.y
    
    # Calculate the corresponding coordinates on the map image
    map_width, map_height = map_image.size
    map_x = int((x / map_label.winfo_width()) * map_width)
    map_y = int((y / map_label.winfo_height()) * map_height)
    
    # Get the selected drone from the dropdown menu
    selected_drone = drone_combobox.get()
    
    # Find the corresponding Drone object
    selected_drone_obj = next((drone for drone in drones if drone.name == selected_drone), None)
    
    # Add the waypoint to the selected drone's list of waypoints
    if selected_drone_obj:
        selected_drone_obj.waypoints.append((map_x, map_y))
        update_waypoints()

# Function to update the waypoints on the map
def update_waypoints():
    # Clear existing waypoints on the map
    map_label.delete("waypoints")
    
    # Draw new waypoints on the map
    for drone in drones:
        for waypoint in drone.waypoints:
            map_label.create_oval(waypoint[0]-5, waypoint[1]-5, waypoint[0]+5, waypoint[1]+5, fill="red", tags="waypoints")

# Function to calculate and display the flight path for the selected drone
def calculate_flight_path():
    # Get the selected drone from the dropdown menu
    selected_drone = drone_combobox.get()
    
    # Find the corresponding Drone object
    selected_drone_obj = next((drone for drone in drones if drone.name == selected_drone), None)
    
    if selected_drone_obj:
        # Dummy implementation: just print the waypoints for now
        print("Flight path for", selected_drone_obj.name, ":", selected_drone_obj.waypoints)

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
map_label = tk.Canvas(middle_frame, width=map_photo.width(), height=map_photo.height())
map_label.create_image(0, 0, anchor=tk.NW, image=map_photo)
map_label.pack(expand=True)

# Bind click event on the map
map_label.bind("<Button-1>", on_map_click)

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

button_settings = tk.Button(right_frame, text="Settings", command=lambda: print("Settings"))
button_settings.pack(pady=5)

button_plan_flight_path = tk.Button(right_frame, text="Plan Flight Path", command=calculate_flight_path)
button_plan_flight_path.pack(pady=5)

# Run the application
root.mainloop()
