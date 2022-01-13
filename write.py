# Encoode and save privateKey to RFID tag
                                                                                                                                                                                                          
#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time
import codecs


reader = SimpleMFRC522()

try:

        text = input('New data:')
        print("Now place your tag to write")

        hex = text
        b64 = codecs.encode(codecs.decode(hex, 'hex'), 'base64').decode()
        print(b64)
        reader.write(b64)
        print("Written")
        print(b64)

finally:
        GPIO.cleanup()
