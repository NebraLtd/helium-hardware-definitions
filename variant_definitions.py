variant_definitions = {
    # Nebra Indoor Hotspot Gen1
    "NEBHNT-IN1" : {
        'SPIBUS': 'spidev1.2',
        'RESET' : 38,
        'MAC' : 'eth0',
        'STATUS': 25,
        'BUTTON': 26,
        'ECCOB': True,
        'TYPE': "Full"
        },

    # Nebra Indoor Hotspot, Old identifier
    "Indoor" : {
        'SPIBUS': 'spidev1.2',
        'RESET' : 38,
        'MAC' : 'eth0',
        'STATUS': 25,
        'BUTTON': 26,
        'ECCOB': True,
        'TYPE': "Full"
        },

    # Nebra Outdoor Hotspot Gen1
    "NEBHNT-OUT1" : {
        'SPIBUS': 'spidev1.2',
        'RESET' : 38,
        'MAC' : 'eth0',
        'STATUS': 25,
        'BUTTON': 26,
        'ECCOB': True,
        'TYPE': "Full"
        },

    # Nebra Outdoor Hotspot Old Identifier
    "Outdoor" : {
        'SPIBUS': 'spidev1.2',
        'RESET' : 38,
        'MAC' : 'eth0',
        'STATUS': 25,
        'BUTTON': 26,
        'ECCOB': True,
        'TYPE': "Full"
        },

    # Nebra Pi 0 Light Hotspot SPI Ethernet
    "NEBHNT-LGT-ZS" : {
        'SPIBUS': 'spidev1.2',
        'RESET' : 22,
        'MAC' : 'wlan0',
        'STATUS': 24,
        'BUTTON': 23,
        'ECCOB': True,
        'TYPE': "Full"
        },

    # Nebra Pi 0 Light Hotspot USB Ethernet
    "NEBHNT-LGT-ZX" : {
        'SPIBUS': 'spidev1.2',
        'RESET' : 22,
        'MAC' : 'wlan0',
        'STATUS': 24,
        'BUTTON': 23,
        'ECCOB': True,
        'TYPE': "Full"
        },

    # Nebra Beaglebone Light Hotspot
    "NEBHNT-BBB" : {
        'SPIBUS': 'spidev1.0',
        'RESET' : 60,
        'MAC' : 'eth0',
        'STATUS': 31,
        'BUTTON': 30,
        'ECCOB': True,
        'TYPE': "Full"
        },

    # Nebra Pocket Beagle Light Hotspot
    "NEBHNT-PBB" : {
        'SPIBUS': 'spidev1.2',
        'RESET' : 60,
        'MAC' : 'wlan0',
        'STATUS': 31,
        'BUTTON': 30,
        'ECCOB': True,
        'TYPE': "Full"
        },

    # Nebra Hotspot HAT Rockpi 4
    "NEBHNT-HHRK4" : {
        'SPIBUS': 'spidev1.0',
        'RESET' : 149,
        'MAC' : 'eth0',
        'STATUS': 156,
        'BUTTON': 154,
        'ECCOB': True
        },

    # Nebra Hotspot HAT RPi 3/4 Full
    "NEBHNT-HHRPI" : {
        'SPIBUS': 'spidev0.0',
        'RESET' : 22,
        'MAC' : 'eth0',
        'STATUS': 24,
        'BUTTON': 23,
        'ECCOB': True
        },

    # Nebra Hotspot HAT RPi Light
    "NEBHNT-HHRPL" : {
        'SPIBUS': 'spidev0.0',
        'RESET' : 22,
        'MAC' : 'eth0',
        'STATUS': 24,
        'BUTTON': 23,
        'ECCOB': True
        },

    # Nebra Hotspot HAT Tinkerboard 1
    "NEBHNT-HHTK" : {
        'SPIBUS': 'spidev2.0',
        'RESET' : 167,
        'MAC' : 'eth0',
        'STATUS': 163,
        'BUTTON': 162,
        'ECCOB': True,
        'TYPE': "Light"
        },

    # Nebra Hotspot HAT Tinkerboard 2
    "NEBHNT-HHTK2" : {
        'SPIBUS': 'spidev2.0',
        'RESET' : 167,
        'MAC' : 'eth0',
        'STATUS': 163,
        'BUTTON': 162,
        'ECCOB': True,
        'TYPE': "Full"
        },

    # RAKwireless Hotspot Miner
    "COMP-RAKHM" : {
        'SPIBUS': 'spidev0.0',
        'RESET' : 17,
        'MAC' : 'wlan0',
        'STATUS': 20,
        'BUTTON': 21,
        'ECCOB': True,
        'TYPE': "Full"
        },

    # Helium Hotspot
    "COMP-HELIUM" : {
        'SPIBUS': 'spidev0.0',
        'RESET' : 17,
        'MAC' : 'wlan0',
        'STATUS': 20,
        'BUTTON': 21,
        'ECCOB': True,
        'TYPE': "Full"
        },

    # DIY Pi Supply Hotspot HAT
    "DIY-PISLGH" : {
        'SPIBUS': 'spidev0.0',
        'RESET' : 22,
        'MAC' : 'eth0',
        'STATUS': 20,
        'BUTTON': 21,
        'ECCOB': False,
        'TYPE': "Light"
        },

    # Nebra Indoor Hotspot
    "DIY-RAK2287" : {
        'SPIBUS': 'spidev0.0',
        'RESET' : 17,
        'MAC' : 'eth0',
        'STATUS': 20,
        'BUTTON': 21,
        'ECCOB': False,
        'TYPE': "Light"
        }
}
