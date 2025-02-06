import smbus
import time

MAX30102_ADDRESS = 0x57  # Default I2C address
LED1_BRIGHTNESS_REG = 0x0C
LED2_BRIGHTNESS_REG = 0x0D

# Initialize I2C bus
bus = smbus.SMBus(1)  # For Raspberry Pi, typically bus 1

def set_led_brightness(led1_brightness, led2_brightness):
    # Set the LED brightness for both Red (LED1) and IR (LED2)
    bus.write_byte_data(MAX30102_ADDRESS, LED1_BRIGHTNESS_REG, led1_brightness)
    bus.write_byte_data(MAX30102_ADDRESS, LED2_BRIGHTNESS_REG, led2_brightness)

# Set LED brightness to maximum (0x1F)
set_led_brightness(0xFF, 0xFF)
time.sleep(5)

# Set LED brightness to lower (for example, 0x10)
set_led_brightness(0x1F, 0x1F)
time.sleep(5)

# Set LED brightness to minimum (0x00)
set_led_brightness(0x00, 0x00)
