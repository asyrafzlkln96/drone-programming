from djitellopy import tello
from time import sleep

me = tello.Tello()
me.connect()
# Get bettery percentage
print(me.get_battery())

me.takeoff()
me.send_rc_control(0, 50, 0, 0)
sleep(2)
me.send_rc_control(0, 0, 0, 30)
sleep(2)
me.send_rc_control(0, 0, 0, 0)
me.land()


