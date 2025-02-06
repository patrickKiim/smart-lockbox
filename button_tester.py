import RPi.GPIO as GPIO
import time
import threading

# Define the button pin
GREEN_BUTTON_PIN = 26

# Create a Lock object to ensure thread safety
gpio_lock = threading.Lock()

# Set up GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
#GPIO.setup(GREEN_BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(GREEN_BUTTON_PIN, GPIO.IN)

# Callback function for button press
def button_callback(channel):
    with gpio_lock:
        print("Button was pressed!")

# Button detection in a separate thread
def button_detection():
    GPIO.add_event_detect(GREEN_BUTTON_PIN, GPIO.RISING, callback=button_callback, bouncetime=200)
    while True:
        time.sleep(0.1)

# Start button detection in a separate thread
button_thread = threading.Thread(target=button_detection)
button_thread.daemon = True  # Allow the thread to exit when the main program exits
button_thread.start()

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")
    GPIO.cleanup()
