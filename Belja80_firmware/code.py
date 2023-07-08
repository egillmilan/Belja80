#ISO LAYOUT

import microcontroller as uC

from kb import KMKKeyboard
from kmk.keys import KC

keyboard = KMKKeyboard()

keyboard.keymap = [
    [KC.ESC,    KC.F1,      KC.F2,      KC.F3,  KC.F4,  KC.F5,  KC.F6,  KC.F7,  KC.F8,      KC.F9,      KC.F10,     KC.F11,     KC.F12,     KC.PSCR,    KC.SLCK,
     KC.GRV,    KC.N1,      KC.N2,      KC.N3,  KC.N4,  KC.N6,  KC.N7,  KC.N8,  KC.N0,      KC.MINS,    KC.EQL,     KC.BSPC,    KC.INS,     KC.HOME,    KC.PAUS,
     KC.TAB,    KC.Q,       KC.W,       KC.E,   KC.R,   KC.N5,  KC.Y,   KC.N9,  KC.O,       KC.P,       KC.LBRC,    KC.RBRC,    KC.DEL,     KC.END,     KC.PGUP,
     KC.CAPS,   KC.A,       KC.S,       KC.D,   KC.F,   KC.T,   KC.U,   KC.I,   KC.L,       KC.SCLN,    KC.QUOT,    KC.NUHS,    KC.NO,      KC.UP,      KC.PGDN,
     KC.LSFT,   KC.NUBS,    KC.Z,       KC.X,   KC.C,   KC.G,   KC.H,   KC.J,   KC.K,       KC.DOT,     KC.SLSH,    KC.RSFT,    KC.ENT,     KC.DOWN,    KC.RGHT,
     KC.LCTL,   KC.LGUI,    KC.LALT,    KC.SPC, KC.V,   KC.B,   KC.N,   KC.M,   KC.COMM,    KC.RALT,    KC.RGUI,    KC.APP,     KC.RCTL,    KC.LEFT,    KC.NO,
    ]
]

if __name__ == '__main__':
    keyboard.go()