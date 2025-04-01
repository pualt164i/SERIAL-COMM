# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 11:13:12 2025

@author: Luis
"""

from pymodbus.client import ModbusSerialClient
import struct

# Configuración del puerto serial (Modbus RTU)
client = ModbusSerialClient(
    #method='rtu',
    port='COM3',          # Puerto COM3 (Windows)
    baudrate=9600,        # Velocidad 9600 bps
    parity='N',           # Sin paridad
    stopbits=1,           # 1 bit de parada
    timeout=2             # Timeout en segundos
)

# Dirección Modbus del dispositivo (slave ID)
slave_id = 1

# Dirección del registro donde comienza el IEEE Float (consulta el manual del P2000-t)
register_address = 32784      # Ejemplo: dirección 0 (ajusta según tu necesidad)

if client.connect():
    try:
        # Leer 2 registros (32 bits = 1 float)
        response = client.read_holding_registers(
            address=register_address,
            count=2,
            slave=slave_id
        )

        if not response.isError():
            # Unir los 2 registros (16 bits cada uno) y convertir a IEEE 754 Float
            raw_data = response.registers
            packed_float = struct.pack('>HH', raw_data[0], raw_data[1])  # Big-endian
            float_value = struct.unpack('>f', packed_float)[0]  # Desempaquetar a float

            print(f"Valor IEEE Float leído: {float_value}")
        else:
            print("Error en la respuesta Modbus:", response)
    except Exception as e:
        print("Error:", e)
    finally:
        client.close()
else:
    print("No se pudo conectar al dispositivo")