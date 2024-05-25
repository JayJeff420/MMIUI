#Simple Drone UI

import tkinter as tk

def display_selected_drones():
    # Function to display selected drones
    pass

def start_surveillance():
    # Function to start surveillance
    pass

def view_map():
    # Function to view the map
    pass

def zoom_in():
    global zoom_factor
    zoom_factor += 0.1
    # Update map (if you have it)

def zoom_out():
    global zoom_factor
    zoom_factor -= 0.1
    # Update map (if you have it)

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

# Add "View Map" button
button_view_map = tk.Button(middle_frame, text="View Map", command=view_map)
button_view_map.pack(pady=10)

# Add widgets to right frame (select drones)
label_select_drones = tk.Label(right_frame, text="Select Drones", font=("Helvetica", 16))
label_select_drones.pack(pady=10)

button_display_selected = tk.Button(right_frame, text="Display Selected Drones", command=display_selected_drones)
button_display_selected.pack(pady=5)

button_start_surveillance = tk.Button(right_frame, text="Start Surveillance", command=start_surveillance)
button_start_surveillance.pack(pady=5)

# Add zoom buttons (optional, if you have a map)
button_zoom_in = tk.Button(right_frame, text="Zoom In", command=zoom_in)
button_zoom_in.pack(pady=5)

button_zoom_out = tk.Button(right_frame, text="Zoom Out", command=zoom_out)
button_zoom_out.pack(pady=5)

# Run the application
root.mainloop()
