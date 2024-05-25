import RPi.GPIO as GPIO
import time

# Set GPIO mode
GPIO.setmode(GPIO.BOARD)

# Define the pin connected to the digital output of the light sensor
LIGHT_SENSOR_PIN = 18

# Set up the pin as an input
GPIO.setup(LIGHT_SENSOR_PIN, GPIO.IN)

# Function to read data from the light sensor
def read_light_sensor():
    # Read digital input from the light sensor
    light_intensity = GPIO.input(LIGHT_SENSOR_PIN)
    return light_intensity

try:
    while True:
        # Read data from the light sensor
        intensity = read_light_sensor()
        print("Light intensity:", intensity)

        # Add any additional logic here based on the light intensity
        
        # Wait for a brief period before reading again
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")
    GPIO.cleanup()  # Clean up GPIO on exit
