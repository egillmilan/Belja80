import microcontroller as uC

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation

class KMKKeyboard(_KMKKeyboard):
    col_pins = (uC.pin.GPIO16, uC.pin.GPIO17, uC.pin.GPIO19, uC.pin.GPIO20, uC.pin.GPIO21, uC.pin.GPIO18, uC.pin.GPIO23, uC.pin.GPIO25, uC.pin.GPIO27, uC.pin.GPIO0, uC.pin.GPIO2, uC.pin.GPIO3, uC.pin.GPIO8, uC.pin.GPIO9, uC.pin.GPIO10)
    row_pins = (uC.pin.GPIO1, uC.pin.GPIO11, uC.pin.GPIO12, uC.pin.GPIO13, uC.pin.GPIO14, uC.pin.GPIO15)
    diode_orientation = DiodeOrientation.COL2ROW