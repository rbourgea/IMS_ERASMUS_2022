import serial
import json
from paho.mqtt import client as mqttClient
import time

def on_connect(client, userdata, flags, rc):
 
    if rc == 0:
 
        print("Connected to broker")
 
        global Connected                #Use global variable
        Connected = True                #Signal connection 
 
    else:
 
        print("Connection failed")

Connected = False #global variable for the state of the connection

# Information about the configuration of the broker
broker_address= "localhost"
port = 1883
user = "mqtt"
password = "client"

serialPort = serial.Serial(port = "COM3", baudrate=9600)
serialString = ""                                           # Used to hold data coming over UART

# Connection to the broker
client = mqttClient.Client("MQTT_IMS")
client.username_pw_set(user, password=password)
client.on_connect= on_connect
client.connect(broker_address, port=port)
client.loop_start()

while Connected != True:    #Wait for connection
    time.sleep(0.1)

try:
    while True:

        # Wait until there is data waiting in the serial buffer
        if(serialPort.in_waiting > 0):

            # Read data out of the buffer until a carraige return / new line is found
            serialString = serialPort.readline()        # type BYTE
            serialString = serialString.decode('Ascii') # Convert BYTE into String
            jsonString = json.dumps(serialString)       # JSON String
            client.publish("Motion", jsonString)        # Publish the JSON String in topic Motion
 
# To disconnect from broker with ctrl + c
except KeyboardInterrupt:   
 
    client.disconnect()
    client.loop_stop()
