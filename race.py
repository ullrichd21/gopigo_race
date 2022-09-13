import time  # import the time library for the sleep function
import gopigo3  # import the GoPiGo3 drivers

GPG = gopigo3.GoPiGo3()  # Create an instance of the GoPiGo3 class. GPG will be the GoPiGo3 object.

def move_inch(inches=1):
    rate = 9
    for i in range(0, inches*rate):
        GPG.set_motor_power(GPG.MOTOR_LEFT + GPG.MOTOR_RIGHT, 100)
        time.sleep(0.01)
        print(f"Moved {round(i/rate, 2)} inch(es)")
def stop():
    GPG.set_motor_power(GPG.MOTOR_LEFT + GPG.MOTOR_RIGHT, 0)
try:
#     while True:
    move_inch(12)
    stop()
except KeyboardInterrupt:  # except the program gets interrupted by Ctrl+C on the keyboard.
    GPG.reset_all()  # Unconfigure the sensors, disable the motors, and restore the LED to the control of the GoPiGo3 firmware.