import BlynkLib
from time import sleep

BLYNK_AUTH = 'YOUR-AUTH-TOKEN'
# initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# register handler for virtual pin V0 write event
@blynk.on("V0")
def v3_write_handler(value):
    buttonValue=value[0]
    print(f'Current button value: {buttonValue}')

# infinite loop that waits for event
while True:
    blynk.run()
     sleep(.5)
