from tkinter import Tk, Frame, Button, Label, PhotoImage
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

# Add your existing GUI elements here

# Run the application
root.mainloop()

      
