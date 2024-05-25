import tkinter as tk
from tkinter import ttk
import time
import random

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
