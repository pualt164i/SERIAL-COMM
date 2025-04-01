# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 11:00:53 2025

@author: Luis
"""

from pymodbus.client import ModbusSerialClient
# from pymodbus.exceptions import ModbusException

client = ModbusSerialClient(
    #methods='rtu',
    port='COM3',
    baudrate=9600,
    stopbits=1,
    bytesize=8,
    parity='N',
    timeout=2
)

if client.connect():
    response = client.read_holding_registers(address=32784, count=2, slave=1)
    
    if not response.isError():
        print("RTU Registers Read:", response.registers)
    else:
        print("RTU Error:", response)
else:
    print("Cant Connected Using RTU")
client.close()
