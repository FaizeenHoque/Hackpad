print("Starting KMK Keyboard")
import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros, Press, Release, Tap, Delay

# Initialize Macros module
macros = Macros()

# Main keyboard instance
keyboard = KMKKeyboard()
keyboard.modules.append(macros)

# Define your pins - based on your schematic:
# SW1=GP0/TX, SW2=GP2/SCK, SW3=GP4/MISO, SW4=GP3/MOSI
PINS = [board.RX, board.SCK, board.MISO, board.MOSI]

# Use KeysScanner for direct pin connections
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
    pull=True
)

# Create macros to open Firefox and Discord
# For Windows: Win+R, type command, Enter
OPEN_FIREFOX = KC.MACRO(
    Press(KC.LGUI),    # Press Windows key
    Tap(KC.R),         # Tap R (opens Run dialog)
    Release(KC.LGUI),  # Release Windows key
    Delay(0),        # Wait for Run dialog to open
    "firefox",         # Type "firefox"
    Tap(KC.ENTER)      # Press Enter
)

OPEN_CMD = KC.MACRO(
    Press(KC.LGUI),    # Press Windows key
    Tap(KC.R),         # Tap R (opens Run dialog)
    Release(KC.LGUI),  # Release Windows key
    Delay(0),        # Wait for Run dialog to open
    "cmd",         # Type "discord"
    Tap(KC.ENTER)      # Press Enter
)

# Define what each switch does:
# SW1(TX)=Open Firefox, SW2(SCK)=Open Discord, SW3(MISO)=C, SW4(MOSI)=D
keyboard.keymap = [
    [OPEN_FIREFOX, OPEN_CMD, KC.C, KC.D]
]

print("Keyboard configured!")
print("SW1=Open Firefox, SW2=Open Discord, SW3=C, SW4=D")
print("Press switches to test!")

if __name__ == '__main__':
    keyboard.go()