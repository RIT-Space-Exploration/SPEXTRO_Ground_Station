"""
File: xbee_handler.py
Org: RIT Space Exploration
Desc:
    XBeeHandler class responsible for capturing telemetry
    streaming across a serial connection.
"""

import threading
import digi.xbee.devices as XBD
from digi.xbee.models.address import XBee16BitAddress

BAUD_RATE = 9600

def run_in_thread(func):
    def wrapper():
        thread = threading.Thread(target=func)
        thread.start()
        return thread
    return wrapper

class XBeeHandler:
    def __init__(self, port_name, remote_addr, callback_var):
        self.con_device = XBD.XBeeDevice(port_name, BAUD_RATE)
        self.remote_device = XBD.RemoteXBeeDevice(self.con_device, XBee16BitAddress.from_hex_string(remote_addr))
        self.callback = callback_var
        self.running = False

        self.con_device.open()
        self.con_device.flush_queues()

    @run_in_thread
    def read_data(self):
        self.running = True

        while self.running:
            telemetry_message = self.con_device.read_data_from(self.remote_device)
            self.callback(telemetry_message.data)

        self.con_device.close()

