import pynput
import time
import keyboard
import pynput.mouse
import colorama
from colorama import Fore, Style, init
from pynput.mouse import Button, Controller
init()
controller = Controller()

def main():
    print(f"{Fore.CYAN}{Style.BRIGHT}hi lol this was made by rob if that matters")
    keybind1 = input("keybind u want to use (use letter): ")
    keybind = str(keybind1)
    gogojuice1 = input("type 0 for go fast and type 1 for 1 second delay: ")
    gogojuice = int(gogojuice1)
    print(f"hold {keybind} to click lol")
    while True:
        if keyboard.is_pressed(f'{keybind}'):
            time.sleep(gogojuice)
            controller.press(Button.left)
            controller.release(Button.left)
main()
