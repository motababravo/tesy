#!/usr/bin/python3

import urllib.request as ur, json
import paho.mqtt.publish as publish

try:
    response = ur.urlopen("http://192.168.78.21/status?_=1589913980044")
    dataReceived = response.read()

    if not dataReceived:
        print("No data received from TESY!")
        quit()

    data = json.loads(dataReceived)

    if not data:
        print("Invalid JSON data received!")
        quit()

    temp = data["gradus"]

    if temp:
        publish.single("solar/tesy/temp", temp, hostname="192.168.78.13")
        print(temp)
    else:
        print("Error reading temperature from TESY!")

except Exception as e:
    print("Connection to TESY failed: Exception: " + str(e))
    quit()
