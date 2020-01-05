import serial_reader
import sys

def handle_incoming_messages(message_b):
    pass

def usage():
    print("Usage: python ground_station.py <port name>")
    exit(1)

def main():

    if not len(sys.argv) == 2:
        usage()

    port_name = sys.argv[1] # str: serial port name

    serial_reader_obj = serial_reader.SerialReader(port_name, handle_incoming_messages)
    serial_reader_thread = serial_reader_obj.read_data()

main()