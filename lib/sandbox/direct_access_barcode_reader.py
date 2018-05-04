import evdev

dev=evdev.InputDevice('/dev/input/by-id/usb-SCANNER_SCANNER_08FF20150112-event-kbd')
reading = ''
for event in dev.read_loop():
    if event.type == evdev.ecodes.EV_KEY and event.value:
        code = evdev.ecodes.KEY[event.code].rpartition("_")[2]
        if code == 'SPACE':
            code = ' '
        if code == 'COMMA':
            code = ','
        if code == 'ENTER':
            print(reading)
            reading = ''
            continue
        reading += code

