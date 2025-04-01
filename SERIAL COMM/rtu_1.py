# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 10:31:25 2025

@author: Luis
"""

from pymodbus.client import ModbusSerialClient

# Connection to device
client = ModbusSerialClient(
    port="COM3",
    #startbit=1,
    #databits=8,
    parity="N",
    stopbits=1,
    #errorcheck="crc",
    baudrate=9600,
    #methods="RTU",
    timeout=2,
)
if client.connect(): # Connection to slave device
    print("Connection Successful")
    response = client.read_holding_registers(address=42514, count=2, slave=1)
    print(response)
    client.close()
else:
    print("Failed to connect to Modbus device")