import keyboard


while True:
  rk=keyboard.record(until="shift")
  keyboard.play(rk,speed_factor=10)
  keyboard.add_hotkey('alt',lambda : exit(0))






