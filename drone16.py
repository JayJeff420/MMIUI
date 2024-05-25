import tkinter as tk
from tkinter import Toplevel, Label, Button
from PIL import Image, ImageTk

from drone14 import display_image

def display_settings():
    # Function to display settings in a new window
    settings_window = tk.Toplevel(root)
    settings_window.title("Drone Settings")
    settings_window.transient(root)  # Set the new window as transient to the main window
    
    settings_label = tk.Label(settings_window, text="Drone Settings", font=("Helvetica", 16))
    settings_label.pack(pady=10)
    
    settings_frame = tk.Frame(settings_window)
    settings_frame.pack(padx=20, pady=10)

    settings_data = [
        ("Flight Mode:", ["Manual", "Auto"]),
        ("Speed Control:", ["Normal", "Slow"]),
        ("Altitude Control:", ["Low", "High"]),
        ("Camera Settings:", ["Auto", "Manual"]),
        ("Flight Path Planning:", ["Off", "On"]),
        ("Battery Management:", ["On", "Off"]),
        ("Obstacle Avoidance:", ["On", "Off"]),
        ("Emergency Stop:", ["Off", "On"]),
        ("Flight Logs:", ["Show", "Hide"])
    ]

    for i, (label_text, options) in enumerate(settings_data):
        label = tk.Label(settings_frame, text=label_text, width=20, anchor="w")
        label.grid(sticky="w", padx=5, pady=2)
        
        var = tk.StringVar(root, options[0])  # Set default value
        option_menu = tk.OptionMenu(settings_frame, var, *options)
        option_menu.grid(row=i, column=1, sticky="w", padx=5, pady=2)

def display_telemetry():
    # Function to display telemetry data in a new window
    telemetry_window = tk.Toplevel(root)
    telemetry_window.title("Telemetry Data")
    telemetry_window.transient(root)  # Set the new window as transient to the main window
    
    telemetry_label = tk.Label(telemetry_window, text="Telemetry Data", font=("Helvetica", 16))
    telemetry_label.pack(pady=10)
    
    telemetry_frame = tk.Frame(telemetry_window)
    telemetry_frame.pack(padx=20, pady=10)

    telemetry_data = [
        ("GPS Coordinates:", "42.3601° N, 71.0589° W"),
        ("Speed:", "25 m/s"),
        ("Altitude:", "100 meters"),
        ("Battery Level:", "75%"),
        ("Temperature:", "20°C"),
        ("Connection Status:", "Connected"),
        ("Signal Strength:", "Strong")
    ]

    for label_text, value in telemetry_data:
        label = tk.Label(telemetry_frame, text=label_text, width=20, anchor="w")
        label.grid(sticky="w", padx=5, pady=2)
        
        value_label = tk.Label(telemetry_frame, text=value, width=10, anchor="w")
        value_label.grid(row=label.grid_info()["row"], column=1, sticky="w", padx=5, pady=2)

def toggle_left_control():
    global left_controls_visible

    if not left_controls_visible:
        left_controls_visible = True
        pitch_up_button.pack(pady=5)
        pitch_down_button.pack(pady=5)
        roll_left_button.pack(pady=5)
        roll_right_button.pack(pady=5)
    else:
        left_controls_visible = False
        pitch_up_button.pack_forget()
        pitch_down_button.pack_forget()
        roll_left_button.pack_forget()
        roll_right_button.pack_forget()

def toggle_right_control():
    global right_controls_visible

    if not right_controls_visible:
        right_controls_visible = True
        throttle_up_button.pack(pady=5)
        throttle_down_button.pack(pady=5)
        yaw_left_button.pack(pady=5)
        yaw_right_button.pack(pady=5)
    else:
        right_controls_visible = False
        throttle_up_button.pack_forget()
        throttle_down_button.pack_forget()
        yaw_left_button.pack_forget()
        yaw_right_button.pack_forget()

def pitch_up():
    print("Pitch Up")

def pitch_down():
    print("Pitch Down")

def roll_left():
    print("Roll Left")

def roll_right():
    print("Roll Right")

def throttle_up():
    print("Throttle Up")

def throttle_down():
    print("Throttle Down")

def yaw_left():
    print("Yaw Left")

def yaw_right():
    print("Yaw Right")

# Function to manage user profiles
def manage_user_profiles():
    profiles_window = Toplevel(root)
    profiles_window.title("User Profiles")
    profiles_window.transient(root)  # Set the new window as transient to the main window

    label = Label(profiles_window, text="User Profile Management", font=("Helvetica", 16))
    label.pack(pady=10)

    # Add profile management options as buttons
    Button(profiles_window, text="Drone Preferences", command=lambda: display_image("")).pack()
    Button(profiles_window, text="Flight History", command=lambda: display_image("")).pack()
    Button(profiles_window, text="Telemetry Preferences", command=lambda: display_image("")).pack()
    Button(profiles_window, text="Camera Settings", command=lambda: display_image("")).pack()
    Button(profiles_window, text="Privacy Settings", command=lambda: display_image("")).pack()
    Button(profiles_window, text="Notifications", command=lambda: display_image("")).pack()
    Button(profiles_window, text="Flight Restrictions", command=lambda: display_image("")).pack()
    Button(profiles_window, text="Emergency Contact Information", command=lambda: display_image("")).pack()
    Button(profiles_window, text="Training/Certification Information", command=lambda: display_image(""))
# Continued code from the previous section...

    Button(profiles_window, text="Training/Certification Information", command=lambda: display_image("")).pack()

# Create main window
root = tk.Tk()
root.title("Surveillance Drone Application")

# Set minimum window size
root.minsize(800, 600)

# Create frames for left, middle, and right sections
left_frame = tk.Frame(root, bg="gray", width=300, height=600)
left_frame.pack_propagate(False)
left_frame.pack(side="left", fill="y")

middle_frame = tk.Frame(root, bg="white", width=800, height=600)
middle_frame.pack_propagate(False)
middle_frame.pack(side="left", expand=True, fill="both")

right_frame = tk.Frame(root, bg="lightgray", width=250, height=600)
right_frame.pack_propagate(False)
right_frame.pack(side="left", fill="y")

# Add widgets to left frame (drone cameras)
label_drone_cameras = tk.Label(left_frame, text="Drone Cameras", font=("Helvetica", 16))
label_drone_cameras.pack(pady=10)

# Create a canvas for the live camera feed placeholder
canvas_width = 280  # Adjust width as needed
canvas_height = 200  # Adjust height as needed
canvas = tk.Canvas(left_frame, width=canvas_width, height=canvas_height, bg="black")
canvas.pack(pady=10)

# Add a placeholder rectangle for the live camera feed
placeholder_width = 240  # Adjust width as needed
placeholder_height = 160  # Adjust height as needed
placeholder_x = (canvas_width - placeholder_width) // 2
placeholder_y = (canvas_height - placeholder_height) // 2
placeholder = canvas.create_rectangle(placeholder_x, placeholder_y, placeholder_x + placeholder_width, placeholder_y + placeholder_height, outline="white", width=2)

# Add text under the placeholder
text_x = canvas_width // 2
text_y = placeholder_y + placeholder_height + 10  # Adjust vertical spacing as needed
canvas.create_text(text_x, text_y, text="Overhead", fill="white", font=("Helvetica", 12))

# Create a canvas for the live camera feed placeholder
canvas_width = 280  # Adjust width as needed
canvas_height = 200  # Adjust height as needed
canvas= tk.Canvas(left_frame, width=canvas_width, height=canvas_height, bg="black")
canvas.pack(pady=10)

# Add a placeholder rectangle for the live camera feed
placeholder_width = 240  # Adjust width as needed
placeholder_height = 160  # Adjust height as needed
placeholder_x = (canvas_width - placeholder_width) // 2
placeholder_y = (canvas_height - placeholder_height) // 2
placeholder = canvas.create_rectangle(placeholder_x, placeholder_y, placeholder_x + placeholder_width, placeholder_y + placeholder_height, outline="white", width=2)

# Add text under the placeholder
text_x = canvas_width // 2
text_y = placeholder_y + placeholder_height + 10  # Adjust vertical spacing as needed
canvas.create_text(text_x, text_y, text="Underbelly", fill="white", font=("Helvetica", 12))

# Load and display map image
map_image=Image.open("C://Users//jayan//OneDrive//Desktop//PS//drone//bangalore_map.png")
map_photo = ImageTk.PhotoImage(map_image)
map_label = tk.Label(middle_frame, image=map_photo)
map_label.image = map_photo  # Keep a reference to prevent garbage collection
map_label.pack(expand=True)

# Add widgets to right frame (select drones)
label_select_drones = tk.Label(right_frame, text="Selected Drone: Drone 1", font=("Helvetica", 16))
label_select_drones.pack(pady=10)

button_display_selected = tk.Button(right_frame, text="Display Selected Drone", command=display_settings)
button_display_selected.pack(pady=5)

button_start_surveillance = tk.Button(right_frame, text="Start Surveillance", command=display_telemetry)
button_start_surveillance.pack(pady=5)

button_settings = tk.Button(right_frame, text="Settings", command=display_settings)
button_settings.pack(pady=5)

# Add telemetry button
button_telemetry = tk.Button(right_frame, text="Telemetry", command=display_telemetry)
button_telemetry.pack(pady=5)

# Add a lot of space between the telemetry button and the right controls button
space_label = tk.Label(right_frame,bg='lightgray', text="")
space_label.pack(pady=138)

# Add left control button
left_controls_visible = False
button_left_control = tk.Button(left_frame, text="Left Control", command=toggle_left_control)
button_left_control.pack(pady=5)

# Add right control button
right_controls_visible = False
button_right_control = tk.Button(right_frame, text="Right Control", command=toggle_right_control)
button_right_control.pack(pady=5)

# Add left control buttons
pitch_up_button = tk.Button(left_frame, text="Pitch Up", command=pitch_up)
pitch_down_button = tk.Button(left_frame, text="Pitch Down", command=pitch_down)
roll_left_button = tk.Button(left_frame, text="Roll Left", command=roll_left)
roll_right_button = tk.Button(left_frame, text="Roll Right", command=roll_right)

# Add right control buttons
throttle_up_button = tk.Button(right_frame, text="Throttle Up", command=throttle_up)
throttle_down_button = tk.Button(right_frame, text="Throttle Down", command=throttle_down)
yaw_left_button = tk.Button(right_frame, text="Yaw Left", command=yaw_left)
yaw_right_button = tk.Button(right_frame, text="Yaw Right", command=yaw_right)

# Add user profile button
button_user_profile = tk.Button(right_frame, text="User Profile", command=manage_user_profiles)
button_user_profile.pack(pady=5)

root.mainloop()
