import machine, onewire, ds18x20, time, sys

ds_pin = machine.Pin(22)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

roms=[]
a=0
while roms==[] and a<10:
    roms = ds_sensor.scan()
    time.sleep(1)
    a+=1
if roms==[]:
    print("No devices found")
    sys.exit()
else:
    print('Found DS devices: ', roms)

while True:
  ds_sensor.convert_temp()
  time.sleep_ms(750)
  for rom in roms:
    print(ds_sensor.read_temp(rom))
  time.sleep(5)