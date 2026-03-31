import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitSide

keyboard = KMKKeyboard()

layers = Layers()
split = Split(
    split_side=SplitSide.LEFT
)

keyboard.modules.append(layers)
keyboard.modules.append(split)

keyboard.col_pins = (board.GP21, board.GP20, board.GP19, board.GP18, board.GP15, board.GP14, board.GP16, board.GP10)
keyboard.row_pins = (board.GP2, board.GP3, board.GP4, board.GP5, board.GP6)

keyboard.diode_orientation = 'COL2ROW'

keyboard.keymap = [
    [
        KC.GRV,   KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,    KC.N6,    KC.N7,
        KC.TAB,   KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,     KC.Y,     KC.NO,
        KC.CAPS,  KC.A,     KC.S,     KC.D,     KC.F,     KC.G,     KC.H,     KC.NO,
        KC.LSFT,  KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,     KC.N,     KC.NO,
        KC.LCTL,  KC.LGUI,  KC.LALT,  KC.MO(1), KC.SPC,   KC.NO,    KC.NO,    KC.NO,
    ],
    [
        KC.ESC,   KC.F1,    KC.F2,    KC.F3,    KC.F4,    KC.F5,    KC.F6,    KC.F7,
        KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,
        KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,
        KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,
        KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,    KC.NO,
    ]
]

if __name__ == '__main__':
    keyboard.go()