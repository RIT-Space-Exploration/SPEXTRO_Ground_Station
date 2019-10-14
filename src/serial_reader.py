"""
File: serial_reader.py
Org: RIT Space Exploration
Desc:
    SerialReader class responsible for capturing telemetry
    streaming across a serial connection.
"""

import serial

"""Create a class named SerialReader that will handle data streaming in over a serial connection using PySerial. This 
class should take in the necessary information to initialize a Serial connection and a variable which will be used as 
a callback. Store the Serial connection object, the callback and a boolean which will be used as a condition (set to 
True) as instance variables (IE: self.xxxx). This class should include the following method: 

read_data(self): This method should, in a while loop using the condition variable as the condition (1) Call .read(
size=2) on the serial connection to grab the size of the incoming message. (2) Convert this raw bytes string to an 
int. (3) Use this size as the size parameter for the next .read(size=message_size) call. (4) pass the bytes string 
returned from the read call into the callback variable. 


"""
class SerialReader:
    def __init__(self, port_name, callback_var):
        self.ser = serial.Serial(port_name)
        self.callback_var = callback_var
        self.bool = True

    def read_data(self):
        while True:
            message_size_b = self.ser.read(size=2)
            message_size = int.from_bytes(size_b)
            message_b = self.ser.read(size=message_size)
            self.callback_var = message_b

