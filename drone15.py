import tkinter as tk
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import Label, ttk
import time
import random
from tkinter import Tk, Frame, Button
from PIL import Image, ImageTk

def toggle_user_profiles():
    global user_profiles_visible
    user_profiles_visible = not user_profiles_visible
    if user_profiles_visible:
        show_user_profiles()
    else:
        hide_user_profiles()

def show_user_profiles():
    for i, button in enumerate(user_profile_buttons):
        button.grid(row=i, column=0, pady=5, padx=10, sticky="ew")
    button_back.grid(row=len(user_profile_buttons), column=0, pady=10, padx=10, sticky="ew")

def hide_user_profiles():
    for button in user_profile_buttons:
        button.grid_forget()
    button_back.grid_forget()

def manage_user_profiles():
    # Function to manage user profiles
    # This could be expanded to include various profile management options
    print("Managing user profiles")

def display_image(image_path):
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo

def close_window():
    root.destroy()

# Create main window
root = Tk()
root.title("Surveillance Drone Application")

# Set minimum window size
root.minsize(800, 600)

# Create frames for left, middle, and right sections
left_frame = Frame(root, bg="gray", width=300, height=600)
left_frame.pack_propagate(False)
left_frame.pack(side="left", fill="y")

middle_frame = Frame(root, bg="white", width=800, height=600)
middle_frame.pack_propagate(False)
middle_frame.pack(side="left", expand=True, fill="both")

right_frame = Frame(root, bg="lightgray", width=250, height=600)
right_frame.pack_propagate(False)
right_frame.pack(side="left", fill="y")

# Add a button for user profiles
user_profiles_visible = False
button_user_profiles = Button(right_frame, text="User Profiles", command=toggle_user_profiles)
button_user_profiles.pack(pady=10)

# Add buttons for user profile options
user_profile_buttons = [
    Button(right_frame, text="Drone Preferences", command=lambda: display_image("")),
    Button(right_frame, text="Flight History", command=lambda: display_image("")),
    Button(right_frame, text="Telemetry Preferences", command=lambda: display_image("")),
    Button(right_frame, text="Camera Settings", command=lambda: display_image("")),
    Button(right_frame, text="Privacy Settings", command=lambda: display_image("")),
    Button(right_frame, text="Notifications", command=lambda: display_image("")),
    Button(right_frame, text="Flight Restrictions", command=lambda: display_image("")),
    Button(right_frame, text="Emergency Contact Information", command=lambda: display_image("")),
    Button(right_frame, text="Training/Certification Information", command=lambda: display_image(""))
]

# Add back button
button_back = Button(right_frame, text="Back", command=close_window)

# Create label for displaying images
image_label = Label(middle_frame)
image_label.pack()

# Hide user profile buttons initially
hide_user_profiles()

root.mainloop()

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

    # Sample telemetry data
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

# Update the rectangle size if needed
def update_placeholder_size():
    canvas.coords(placeholder, placeholder_x, placeholder_y, placeholder_x + placeholder_width, placeholder_y + placeholder_height)


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
canvas.create_text(text_x, text_y, text="Underbelly", fill="white", font=("Helvetica", 12))

# Update the rectangle size if needed
def update_placeholder_size():
    canvas.coords(placeholder, placeholder_x, placeholder_y, placeholder_x + placeholder_width, placeholder_y + placeholder_height)

# Example of updating the placeholder size (commented out)
# placeholder_width = 200
# placeholder_height = 120
# update_placeholder_size()

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


# Run the application
root.mainloop()


class MissionPlanner:
    def __init__(self):
        self.mission_objective = None
        self.area_of_interest = None
        self.altitude = None
        self.speed = None
        self.waypoints = []

    def set_mission_objective(self, objective):
        objectives = [
            "Aerial Photography and Videography",
            "Surveillance and Monitoring",
            "Mapping and Surveying",
            "Search and Rescue",
            "Precision Agriculture"
        ]
        if objective not in objectives:
            raise ValueError("Invalid mission objective. Choose from: {}".format(objectives))
        self.mission_objective = objective

    def set_area_of_interest(self, area):
        self.area_of_interest = area

    def set_flight_parameters(self, altitude, speed):
        self.altitude = altitude
        self.speed = speed

    def add_waypoint(self, waypoint):
        self.waypoints.append(waypoint)

    def generate_flight_plan(self):
        if not all([self.mission_objective, self.area_of_interest, self.altitude, self.speed, self.waypoints]):
            raise ValueError("Mission objective, area of interest, altitude, speed, and waypoints must be set before generating a flight plan")
        
        # Your flight planning logic here
        flight_plan = {
            "mission_objective": self.mission_objective,
            "area_of_interest": self.area_of_interest,
            "altitude": self.altitude,
            "speed": self.speed,
            "waypoints": self.waypoints
        }
        return flight_plan

class SafetyModule:
    def __init__(self):
        pass

    def check_weather_conditions(self):
        # Simulated weather conditions for demonstration
        return {
            "temperature": random.uniform(20, 30),  # in degrees Celsius
            "wind_speed": random.uniform(0, 20),    # in m/s
            "precipitation": random.choice(["None", "Light", "Moderate", "Heavy"])
        }

    def check_airspace_restrictions(self):
        # Simulated airspace restrictions for demonstration
        return [
            "No-fly zone over Central Park, New York"
        ]

    def check_potential_hazards(self):
        # Simulated potential hazards for demonstration
        return [
            "Construction crane near waypoint 2"
        ]

class PayloadModule:
    def __init__(self):
        self.payload = []
        self.payload_enabled = False

    def select_payload(self, payload_type):
        # Simulated payload selection for demonstration
        payloads = ["Camera", "Thermal Imaging Camera", "LiDAR"]
        if payload_type not in payloads:
            raise ValueError("Invalid payload type. Choose from: {}".format(payloads))
        self.payload.append(payload_type)

    def remove_payload(self, payload_type):
        if payload_type in self.payload:
            self.payload.remove(payload_type)
        else:
            raise ValueError("Payload type not found")

    def toggle_payload_status(self):
        self.payload_enabled = not self.payload_enabled

    def get_payload_list(self):
        return self.payload

    def is_payload_enabled(self):
        return self.payload_enabled

class BatteryManagementModule:
    def __init__(self, initial_charge, consumption_rate):
        self.initial_charge = initial_charge
        self.charge_left = initial_charge
        self.consumption_rate = consumption_rate

    def update_consumption(self, distance):
        consumption = distance * self.consumption_rate
        self.charge_left -= consumption
        if self.charge_left < 0:
            self.charge_left = 0

    def get_battery_charge(self):
        return self.initial_charge

    def get_battery_consumption(self):
        return self.initial_charge - self.charge_left

    def get_battery_charge_left(self):
        return self.charge_left

    def get_distance_remaining(self):
        return self.charge_left / self.consumption_rate

class DataCollectionModule:
    def __init__(self):
        self.data = []

    def collect_data(self):
        # Simulate data collection from sensors
        sensor_data = {
            "timestamp": time.time(),
            "temperature": random.uniform(20, 30),
            "humidity": random.uniform(40, 60),
            "altitude": random.uniform(0, 100),
            "pressure": random.uniform(900, 1100)
        }
        self.data.append(sensor_data)

    def get_latest_data(self):
        if not self.data:
            return None
        return self.data[-1]

class CommunicationControlModule:
    def __init__(self):
        self.connected = False

    def connect(self):
        # Simulate connecting to the drone
        print("Connecting to drone...")
        time.sleep(1)
        self.connected = True
        print("Connected to drone")

    def disconnect(self):
        # Simulate disconnecting from the drone
        print("Disconnecting from drone...")
        time.sleep(1)
        self.connected = False
        print("Disconnected from drone")

    def send_command(self, command):
        if not self.connected:
            raise ValueError("Not connected to drone")

        # Simulate sending command to the drone
        print(f"Sending command to drone: {command}")
        time.sleep(1)
        print("Command sent successfully")

class DroneGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Drone Mission Planner")

        # Mission Planner Section
        self.create_mission_planner_section()

        # Safety Check Section
        self.create_safety_check_section()

        # Payload Section
        self.create_payload_section()

        # Battery Management Section
        self.create_battery_management_section()

        # Data Collection Section
        self.create_data_collection_section()

        # Communication Control Section
        self.create_communication_control_section()

    def create_mission_planner_section(self):
        frame = ttk.LabelFrame(self.root, text="Mission Planner")
        frame.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        ttk.Label(frame, text="Mission Objective:").grid(row=0, column=0, sticky="w")
        self.mission_objective_entry = ttk.Entry(frame, width=30)
        self.mission_objective_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(frame, text="Area of Interest:").grid(row=1, column=0, sticky="w")
        self.area_of_interest_entry = ttk.Entry(frame, width=30)
        self.area_of_interest_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(frame, text="Altitude (meters):").grid(row=2, column=0, sticky="w")
        self.altitude_entry = ttk.Entry(frame, width=10)
        self.altitude_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(frame, text="Distance Traveled (meters):").grid(row=0, column=1, sticky="w")
        self.altitude_entry = ttk.Entry(frame, width=10)
        self.altitude_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(frame, text="Speed (m/s):").grid(row=3, column=0, sticky="w")
        self.speed_entry = ttk.Entry(frame, width=10)
        self.speed_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")

        ttk.Label(frame, text="Waypoints:").grid(row=4, column=0, sticky="w")
        self.waypoints_text = tk.Text(frame, width=30, height=5)
        self.waypoints_text.grid(row=4, column=1, padx=5, pady=5, sticky="w")

        self.generate_button = ttk.Button(frame, text="Generate Flight Plan", command=self.generate_flight_plan)
        self.generate_button.grid(row=5, columnspan=2, pady=5)

    def create_safety_check_section(self):
        frame = ttk.LabelFrame(self.root, text="Safety Check")
        frame.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.weather_conditions_label = ttk.Label(frame, text="")
        self.weather_conditions_label.grid(row=0, columnspan=2, sticky="w")

        self.airspace_restrictions_label = ttk.Label(frame, text="")
        self.airspace_restrictions_label.grid(row=1, columnspan=2, sticky="w")

        self.hazards_label = ttk.Label(frame, text="")
        self.hazards_label.grid(row=2, columnspan=2, sticky="w")

        self.check_safety_button = ttk.Button(frame, text="Check Safety", command=self.check_safety)
        self.check_safety_button.grid(row=3, columnspan=2, pady=5)

    def create_payload_section(self):
        frame = ttk.LabelFrame(self.root, text="Payload Module")
        frame.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        self.payload_listbox = tk.Listbox(frame, width=30, height=3)
        self.payload_listbox.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.select_payload_entry = ttk.Entry(frame, width=20)
        self.select_payload_entry.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.select_payload_button = ttk.Button(frame, text="Select Payload", command=self.select_payload)
        self.select_payload_button.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        self.remove_payload_entry = ttk.Entry(frame, width=20)
        self.remove_payload_entry.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.remove_payload_button = ttk.Button(frame, text="Remove Payload", command=self.remove_payload)
        self.remove_payload_button.grid(row=2, column=1, padx=5, pady=5, sticky="w")

        self.toggle_payload_button = ttk.Button(frame, text="Toggle Payload Status", command=self.toggle_payload_status)
        self.toggle_payload_button.grid(row=3, columnspan=2, pady=5)

    def create_battery_management_section(self):
        frame = ttk.LabelFrame(self.root, text="Battery Management")
        frame.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.distance_entry = ttk.Entry(frame, width=10)
        self.distance_entry.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        ttk.Label(frame, text="Distance Traveled (meters):").grid(row=0, column=1, sticky="w")

        self.update_battery_button = ttk.Button(frame, text="Update Battery", command=self.update_battery)
        self.update_battery_button.grid(row=1, columnspan=2, pady=5)

        self.battery_info_label = ttk.Label(frame, text="")
        self.battery_info_label.grid(row=2, columnspan=2, sticky="w")

    def create_data_collection_section(self):
        frame = ttk.LabelFrame(self.root, text="Data Collection")
        frame.grid(row=0, column=2, padx=10, pady=5, sticky="w")

        self.collect_data_button = ttk.Button(frame, text="Collect Data", command=self.collect_data)
        self.collect_data_button.grid(row=0, columnspan=2, pady=5)

        self.latest_data_label = ttk.Label(frame, text="")
        self.latest_data_label.grid(row=1, columnspan=2, sticky="w")

    def create_communication_control_section(self):
        frame = ttk.LabelFrame(self.root, text="Communication Control")
        frame.grid(row=1, column=2, padx=10, pady=5, sticky="w")

        self.connect_button = ttk.Button(frame, text="Connect", command=self.connect)
        self.connect_button.grid(row=0, column=0, padx=5, pady=5)

        self.send_command_entry = ttk.Entry(frame, width=20)
        self.send_command_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.send_command_button = ttk.Button(frame, text="Send Command", command=self.send_command)
        self.send_command_button.grid(row=0, column=2, padx=5, pady=5, sticky="w")

        self.disconnect_button = ttk.Button(frame, text="Disconnect", command=self.disconnect)
        self.disconnect_button.grid(row=0, column=3, padx=5, pady=5)

    def generate_flight_plan(self):
        mission_planner = MissionPlanner()
        mission_planner.set_mission_objective(self.mission_objective_entry.get())
        mission_planner.set_area_of_interest(self.area_of_interest_entry.get())
        mission_planner.set_flight_parameters(int(self.altitude_entry.get()), int(self.speed_entry.get()))
        waypoints_text = self.waypoints_text.get("1.0", tk.END)
        waypoints = waypoints_text.strip().split("\n")
        for waypoint in waypoints:
            mission_planner.add_waypoint(waypoint)
        flight_plan = mission_planner.generate_flight_plan()
        print("Flight Plan Generated:", flight_plan)

    def check_safety(self):
        safety_module = SafetyModule()
        weather_conditions = safety_module.check_weather_conditions()
        airspace_restrictions = safety_module.check_airspace_restrictions()
        potential_hazards = safety_module.check_potential_hazards()
        self.weather_conditions_label.config(text="Weather Conditions: " + str(weather_conditions))
        self.airspace_restrictions_label.config(text="Airspace Restrictions: " + str(airspace_restrictions))
        self.hazards_label.config(text="Potential Hazards: " + str(potential_hazards))

    def select_payload(self):
        payload_module = PayloadModule()
        payload_module.select_payload(self.select_payload_entry.get())
        self.update_payload_listbox(payload_module.get_payload_list())

    def remove_payload(self):
        payload_module = PayloadModule()
        try:
            payload_module.remove_payload(self.remove_payload_entry.get())
            self.update_payload_listbox(payload_module.get_payload_list())
        except ValueError as e:
            print(e)


    def toggle_payload_status(self):
        payload_module = PayloadModule()
        payload_module.toggle_payload_status()
        payload_status = "Enabled" if payload_module.is_payload_enabled() else "Disabled"
        print("Payload Status:", payload_status)

    def update_payload_listbox(self, payload_list):
        self.payload_listbox.delete(0, tk.END)
        for payload in payload_list:
            self.payload_listbox.insert(tk.END, payload)

    def update_battery(self):
        battery_module = BatteryManagementModule(100, 0.1)
        distance_traveled = int(self.distance_entry.get())
        battery_module.update_consumption(distance_traveled)
        battery_info = f"Battery Charge: {battery_module.get_battery_charge()}%\n" \
                       f"Battery Consumption: {battery_module.get_battery_consumption()}%\n" \
                       f"Battery Charge Left: {battery_module.get_battery_charge_left()}%\n" \
                       f"Distance Remaining: {battery_module.get_distance_remaining()} meters"
        self.battery_info_label.config(text=battery_info)

    def collect_data(self):
        data_module = DataCollectionModule()
        for _ in range(5):  # Collect data 5 times
            data_module.collect_data()
            time.sleep(1)  # Simulate data collection interval
        latest_data = data_module.get_latest_data()
        if latest_data:
            latest_data_str = ""
            for key, value in latest_data.items():
                latest_data_str += f"{key}: {value}\n"
            self.latest_data_label.config(text=latest_data_str)
        else:
            self.latest_data_label.config(text="No data collected yet.")

    def connect(self):
        communication_module = CommunicationControlModule()
        communication_module.connect()

    def disconnect(self):
        communication_module = CommunicationControlModule()
        communication_module.disconnect()

    def send_command(self):
        communication_module = CommunicationControlModule()
        command = self.send_command_entry.get()
        try:
            communication_module.send_command(command)
        except ValueError as e:
            print(e)

def main():
    root = tk.Tk()
    app = DroneGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()