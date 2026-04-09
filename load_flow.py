
# Simple load flow example

buses = {
    "Bus1": 1.0,
    "Bus2": 0.98,
    "Bus3": 0.95
}

for bus, voltage in buses.items():
    print(f"{bus} Voltage: {voltage} pu")
