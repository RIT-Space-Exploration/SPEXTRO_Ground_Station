"""
File: serial_reader.py
Org: RIT Space Exploration
Desc:
    SerialReader class responsible for capturing telemetry
    streaming across a serial connection.
"""

import serial
import threading

def run_in_thread(func):
    def wrapper():
        thread = threading.Thread(target=func)
        thread.start()
        return thread
    return wrapper

class SerialReader:
    def __init__(self, port_name, callback_var):
        self.ser = serial.Serial(port_name)
        self.callback = callback_var
        self.running = True

        self.ser.open()

    @run_in_thread
    def read_data(self):
        while self.running:
            message_size_b = self.ser.read(size=2)
            message_size = int.from_bytes(message_size_b)
            message_b = self.ser.read(size=message_size)
            self.callback(message_b)
        self.ser.close()

