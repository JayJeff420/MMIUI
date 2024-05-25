#Drone UI with zoom in icon and customisable settings
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Define options for each setting
flight_modes = ["Manual", "Automatic"]
speeds = ["Slow", "Normal", "Fast"]
altitudes = ["Low", "Medium", "High"]
camera_settings = ["Auto", "Manual"]
flight_path_planning = ["On", "Off"]
battery_management = ["On", "Off"]
obstacle_avoidance = ["On", "Off"]
emergency_stop = ["On", "Off"]
flight_logs = ["Show", "Hide"]

def display_settings():
    # Function to display settings in a new window
    settings_window = tk.Toplevel(root)
    settings_window.title("Drone Settings")
    
    settings_label = tk.Label(settings_window, text="Drone Settings", font=("Helvetica", 16))
    settings_label.pack(pady=10)
    
    settings_frame = tk.Frame(settings_window)
    settings_frame.pack(padx=20, pady=10)

    # Dictionary to store dropdown menus
    dropdown_menus = {}

    settings_data = [
        ("Flight Mode:", flight_modes),
        ("Speed Control:", speeds),
        ("Altitude Control:", altitudes),
        ("Camera Settings:", camera_settings),
        ("Flight Path Planning:", flight_path_planning),
        ("Battery Management:", battery_management),
        ("Obstacle Avoidance:", obstacle_avoidance),
        ("Emergency Stop:", emergency_stop),
        ("Flight Logs:", flight_logs)
    ]

    for i, (label_text, options) in enumerate(settings_data):
        label = tk.Label(settings_frame, text=label_text, width=20, anchor="w")
        label.grid(row=i, column=0, sticky="w", padx=5, pady=2)

        # Create dropdown menu
        var = tk.StringVar(settings_frame)
        var.set(options[0])  # Default value
        dropdown_menu = ttk.Combobox(settings_frame, textvariable=var, values=options, state="readonly")
        dropdown_menu.grid(row=i, column=1, sticky="w", padx=5, pady=2)
        dropdown_menus[label_text] = var

    # Function to print selected options
    def print_selected_options():
        for label_text, var in dropdown_menus.items():
            print(label_text, var.get())

    # Button to print selected options
    button_print_options = tk.Button(settings_frame, text="Print Selected Options", command=print_selected_options)
    button_print_options.grid(row=len(settings_data), columnspan=2, pady=10)

def on_drag_start(event):
    global start_x, start_y
    start_x = event.x
    start_y = event.y

def on_drag_motion(event):
    global start_x, start_y
    x, y = event.x, event.y
    delta_x = x - start_x
    delta_y = y - start_y
    map_label.place(x=map_label.winfo_x() + delta_x, y=map_label.winfo_y() + delta_y)
    start_x = x
    start_y = y

def on_drag_release(event):
    pass

def zoom_in():
    global zoom_factor
    zoom_factor *= 1.1  # Increase zoom factor by 10%
    update_map()

def zoom_out():
    global zoom_factor
    zoom_factor /= 1.1  # Decrease zoom factor by 10%
    update_map()

def update_map():
    global map_image, map_photo, map_label, zoom_factor
    new_width = int(original_width * zoom_factor)
    new_height = int(original_height * zoom_factor)
    resized_image = map_image.resize((new_width, new_height), Image.BICUBIC)
    map_photo = ImageTk.PhotoImage(resized_image)
    map_label.config(image=map_photo)
    map_label.image = map_photo

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
original_width, original_height = map_image.size
zoom_factor = 1.0

map_photo = ImageTk.PhotoImage(map_image)
map_label = tk.Label(middle_frame, image=map_photo)
map_label.pack(expand=True)


# Add drag functionality to the map label
map_label.bind("<ButtonPress-1>", on_drag_start)
map_label.bind("<B1-Motion>", on_drag_motion)
map_label.bind("<ButtonRelease-1>", on_drag_release)


# Add button to display selected drone settings
button_display_selected = tk.Button(right_frame, text="Settings", command=display_settings)
button_display_selected.pack(pady=5)

# Add zoom buttons
zoom_button_frame = tk.Frame(right_frame)
zoom_button_frame.pack(pady=5)

button_zoom_in = tk.Button(zoom_button_frame, text="+", command=zoom_in)
button_zoom_in.pack(side="left")

button_zoom_out = tk.Button(zoom_button_frame, text="-", command=zoom_out)
button_zoom_out.pack(side="left")

# Run the application
root.mainloop()


