import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitType
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

layers = Layers()
split = Split(
    split_side=SplitSide.RIGHT
)
encoder_handler = EncoderHandler()

keyboard.modules.append(layers)
keyboard.modules.append(split)
keyboard.modules.append(encoder_handler)

keyboard.col_pins = (board.GP21, board.GP20, board.GP19, board.GP18, board.GP15, board.GP14, board.GP16, board.GP10)
keyboard.row_pins = (board.GP2, board.GP3, board.GP4, board.GP5, board.GP6)

keyboard.diode_orientation = 'COL2ROW'
encoder_handler.pins = (
    (board.GP1, board.GP0, None),
)

encoder_handler.map = [
    ((KC.VOLU, KC.VOLD,),),
    ((KC.PGDN, KC.PGUP,),)
]

keyboard.keymap = [
    [
        KC.N8,     KC.N9,     KC.N0,     KC.MINS,   KC.EQL,    KC.BSPC,   KC.NO,     KC.HOME,
        KC.U,      KC.I,      KC.O,      KC.P,      KC.LBRC,   KC.RBRC,   KC.BSLS,   KC.PGUP,
        KC.J,      KC.K,      KC.L,      KC.SCLN,   KC.QUOT,   KC.ENT,    KC.NO,     KC.PGDN,
        KC.M,      KC.COMM,   KC.DOT,    KC.SLSH,   KC.RSFT,   KC.UP,     KC.NO,     KC.END,
        KC.SPC,    KC.RALT,   KC.RGUI,   KC.RCTL,   KC.LEFT,   KC.DOWN,   KC.RGHT,   KC.NO,
    ],
    [
        KC.F8,     KC.F9,     KC.F10,    KC.F11,    KC.F12,    KC.DEL,    KC.NO,     KC.NO,
        KC.NO,     KC.NO,     KC.NO,     KC.NO,     KC.LCBR,   KC.RCBR,   KC.PIPE,   KC.NO,
        KC.NO,     KC.NO,     KC.NO,     KC.COLN,   KC.DQUO,   KC.NO,     KC.NO,     KC.NO,
        KC.NO,     KC.LABK,   KC.RABK,   KC.QUES,   KC.TRNS,   KC.PGUP,   KC.NO,     KC.NO,
        KC.ENT,    KC.NO,     KC.NO,     KC.NO,     KC.HOME,   KC.PGDN,   KC.END,    KC.NO,
    ]
]

if __name__ == '__main__':
    keyboard.go()